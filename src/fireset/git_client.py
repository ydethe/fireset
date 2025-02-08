from dulwich import porcelain

from . import settings

repo = porcelain.clone(
    str(settings.repo_url), "repo", username="fireset_client", password=settings.repo_token
)
