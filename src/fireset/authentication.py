from aiohttp import web
from typing import Optional, Tuple
import base64
import hashlib
import hmac
import os
from datetime import datetime, timedelta

class AuthenticationManager:
    def __init__(self):
        self.secret_key = os.environ.get('SECRET_KEY', os.urandom(32))
        self.users = {}  # In production, this should be in a database
        
    async def authenticate(self, request: web.Request) -> Tuple[bool, Optional[str]]:
        """Authenticate a request using Basic Authentication"""
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return False, None
            
        try:
            auth_type, auth_string = auth_header.split(' ', 1)
            if auth_type.lower() != 'basic':
                return False, None
                
            credentials = base64.b64decode(auth_string).decode('utf-8')
            username, password = credentials.split(':', 1)
            
            # In production, verify against secure database
            if self.verify_credentials(username, password):
                return True, username
                
        except Exception as e:
            return False, None
            
        return False, None
        
    def verify_credentials(self, username: str, password: str) -> bool:
        """Verify username and password"""
        # In production, use proper password hashing and database lookup
        return True  # For development purposes
        
    def generate_token(self, username: str) -> str:
        """Generate an authentication token"""
        timestamp = datetime.utcnow().timestamp()
        message = f"{username}:{timestamp}".encode()
        signature = hmac.new(self.secret_key, message, hashlib.sha256).hexdigest()
        return f"{username}:{timestamp}:{signature}"
        
    def verify_token(self, token: str) -> bool:
        """Verify an authentication token"""
        try:
            username, timestamp, signature = token.split(':')
            message = f"{username}:{timestamp}".encode()
            expected_signature = hmac.new(self.secret_key, message, hashlib.sha256).hexdigest()
            return hmac.compare_digest(signature, expected_signature)
        except:
            return False

    @web.middleware
    async def auth_middleware(self, request: web.Request, handler):
        """Middleware to handle authentication"""
        if request.method == 'OPTIONS':
            return await handler(request)
            
        is_authenticated, username = await self.authenticate(request)
        if not is_authenticated:
            return web.Response(
                status=401,
                headers={'WWW-Authenticate': 'Basic realm="CardDAV Server"'}
            )
            
        request['username'] = username
        return await handler(request)
