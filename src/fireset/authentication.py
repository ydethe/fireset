import functools
import inspect
import typing as T
from dataclasses import dataclass

from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette_auth_toolkit.base.backends import BaseBasicAuth
from starlette_auth_toolkit.cryptography import PBKDF2Hasher

from .database import get_contact_from_email


_P = T.ParamSpec("_P")

# Password hasher
hasher = PBKDF2Hasher()


def authenticated(func: T.Callable[_P, T.Any]) -> T.Callable[_P, T.Any]:
    """Decorator that checks whether the request is authenticated,
    and ig the user has the right to access the resource

    """
    sig = inspect.signature(func)
    for idx, parameter in enumerate(sig.parameters.values()):
        if parameter.name == "request" or parameter.name == "websocket":
            break
    else:
        raise Exception(f'No "request" or "websocket" argument on function "{func}"')

    # Handle async request/response functions.
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs) -> T.Any:
        request = kwargs.get("request", args[idx] if idx < len(args) else None)
        assert isinstance(request, Request)
        user: BookUser = request.user
        user_id = int(request.path_params.get("user_id", -1))

        if "authenticated" not in request.auth.scopes or user.id != user_id:
            raise HTTPException(status_code=403)

        return await func(*args, **kwargs)

    return async_wrapper


@dataclass
class BookUser:
    id: int
    email: str
    password: str
    is_authenticated: bool

    @classmethod
    def from_db(cls, email: str) -> "BookUser":
        db_contact = get_contact_from_email(email)
        if db_contact is None:
            return None

        if db_contact.hashed_password is None:
            return None

        res = cls(
            id=db_contact.id,
            email=email,
            password=db_contact.hashed_password,
            is_authenticated=False,
        )

        return res


# Authentication backend
class BasicAuth(BaseBasicAuth):
    async def find_user(self, username: str):
        u = BookUser.from_db(email=username)
        return u

    async def verify_password(self, user: BookUser, password: str):
        user.is_authenticated = await hasher.verify(password, user.password)
        return user.is_authenticated
