from aiohttp import web
import logging
from typing import Dict, Optional
from .authentication import AuthenticationManager
from .database import Database
import xml.etree.ElementTree as ElementTree
from pathlib import Path
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

NAMESPACES = {
    'DAV:': 'D',
    'urn:ietf:params:xml:ns:carddav': 'C',
    'http://calendarserver.org/ns/': 'CS'
}

class CardDAVServer:
    def __init__(self):
        self.auth_manager = AuthenticationManager()
        self.database = Database()
        self.app = web.Application()
        self.setup_routes()
        self.app.middlewares.append(self.auth_manager.auth_middleware)
        self.app.on_startup.append(self.startup)
    
    def setup_routes(self):
        self.app.router.add_route('PROPFIND', '/{tail:.*}', self.handle_propfind)
        self.app.router.add_route('REPORT', '/{tail:.*}', self.handle_report)
        self.app.router.add_route('GET', '/{tail:.*}', self.handle_get)
        self.app.router.add_route('PUT', '/{tail:.*}', self.handle_put)
        self.app.router.add_route('DELETE', '/{tail:.*}', self.handle_delete)
        self.app.router.add_route('OPTIONS', '/{tail:.*}', self.handle_options)
        
    async def startup(self, app):
        """Initialize the database on startup"""
        await self.database.initialize()

    async def handle_propfind(self, request):
        """Handle PROPFIND requests for WebDAV property discovery"""
        depth = request.headers.get('Depth', '0')
        try:
            body = await request.text()
            root = ElementTree.fromstring(body) if body else None
            
            # Basic response structure
            response = {
                'DAV:multistatus': {
                    'DAV:response': {
                        'DAV:href': request.path,
                        'DAV:propstat': {
                            'DAV:prop': {},
                            'DAV:status': 'HTTP/1.1 200 OK'
                        }
                    }
                }
            }
            
            return web.Response(
                text=self._dict_to_xml(response),
                content_type='application/xml',
                status=207
            )
        except Exception as e:
            logger.error(f"PROPFIND error: {str(e)}")
            return web.Response(status=500)

    async def handle_report(self, request):
        """Handle REPORT requests for CardDAV queries"""
        try:
            body = await request.text()
            # Process REPORT request
            return web.Response(status=200)
        except Exception as e:
            logger.error(f"REPORT error: {str(e)}")
            return web.Response(status=500)

    async def handle_get(self, request):
        """Handle GET requests for retrieving vCards"""
        return web.Response(text="Not implemented", status=501)

    async def handle_put(self, request):
        """Handle PUT requests for creating/updating vCards"""
        return web.Response(text="Not implemented", status=501)

    async def handle_delete(self, request):
        """Handle DELETE requests for removing vCards"""
        return web.Response(text="Not implemented", status=501)

    async def handle_options(self, request):
        """Handle OPTIONS requests for discovering server capabilities"""
        headers = {
            'DAV': '1, 2, addressbook',
            'Allow': 'OPTIONS, PROPFIND, REPORT, GET, PUT, DELETE'
        }
        return web.Response(headers=headers)

    def _dict_to_xml(self, data: Dict) -> str:
        """Convert dictionary to XML string"""
        # Basic XML conversion implementation
        return '<?xml version="1.0" encoding="utf-8"?><D:multistatus xmlns:D="DAV:"/>'

    def run(self, host: str = '0.0.0.0', port: int = 8080):
        """Run the CardDAV server"""
        web.run_app(self.app, host=host, port=port)

if __name__ == '__main__':
    server = CardDAVServer()
    server.run()
