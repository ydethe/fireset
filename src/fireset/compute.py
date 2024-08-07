import http.server
import urllib.parse
import os
import xml.etree.ElementTree as ET
import datetime

from . import logger


# Directory to store vCards
STORAGE_DIR = "./tests/vcards/"

# Ensure the storage directory exists
os.makedirs(STORAGE_DIR, exist_ok=True)


class CardDAVRequestHandler(http.server.BaseHTTPRequestHandler):
    def _send_response(self, status_code, headers=None, body=None):
        self.send_response(status_code)
        if headers:
            for header, value in headers.items():
                self.send_header(header, value)
        self.end_headers()
        if body:
            self.wfile.write(body)

    def _list_vcards(self):
        """List all vCards in the storage directory."""
        vcards = os.listdir(STORAGE_DIR)
        return [vcard[:-4] for vcard in vcards if vcard.endswith(".vcf")]

    def _read_vcard(self, vcard_id):
        """Read a vCard by its ID."""
        vcard_path = os.path.join(STORAGE_DIR, vcard_id + ".vcf")
        if os.path.exists(vcard_path):
            with open(vcard_path, "rb") as vcard_file:
                return vcard_file.read()
        return None

    def _write_vcard(self, vcard_id, vcard_data):
        """Write a vCard to the storage directory."""
        vcard_path = os.path.join(STORAGE_DIR, vcard_id + ".vcf")
        with open(vcard_path, "wb") as vcard_file:
            vcard_file.write(vcard_data)

    def _delete_vcard(self, vcard_id):
        """Delete a vCard by its ID."""
        vcard_path = os.path.join(STORAGE_DIR, vcard_id + ".vcf")
        if os.path.exists(vcard_path):
            os.remove(vcard_path)
            return True
        return False

    def do_OPTIONS(self):
        """Handle OPTIONS requests."""
        self._send_response(
            200,
            headers={
                "Allow": "OPTIONS, GET, PUT, DELETE, PROPFIND, REPORT",
                "DAV": "1, 3, addressbook",
                "Content-Length": "0",
            },
        )

    def do_PROPFIND(self):
        """Handle PROPFIND requests to list address books or vCards."""
        depth = self.headers.get("Depth", "0")
        content_length = int(self.headers.get("Content-Length", 0))
        request_body = self.rfile.read(content_length)
        if content_length > 0:
            try:
                # Parse the XML request
                root = ET.fromstring(request_body)
                namespace = {"D": "DAV:"}
                propfind = root.find("D:prop", namespace)
            except ET.ParseError:
                self._send_response(400)
                return
        else:
            propfind = None

        logger.debug(f"{propfind}")

        if depth == "0":
            # Listing collections
            response = '<?xml version="1.0" encoding="UTF-8"?>\n'
            response += '<D:multistatus xmlns:D="DAV:">\n'
            response += "  <D:response>\n"
            response += f"    <D:href>{self.path}</D:href>\n"
            response += "    <D:propstat>\n"
            response += "      <D:prop>\n"
            response += "        <D:resourcetype>\n"
            response += "          <D:collection/>\n"
            response += "        </D:resourcetype>\n"
            response += "        <D:displayname>vCards</D:displayname>\n"
            response += "      </D:prop>\n"
            response += "      <D:status>HTTP/1.1 200 OK</D:status>\n"
            response += "    </D:propstat>\n"
            response += "  </D:response>\n"
            response += "</D:multistatus>"

            self._send_response(
                207,
                headers={"Content-Type": 'application/xml; charset="utf-8"'},
                body=response.encode("utf-8"),
            )

        elif depth == "1":
            # Listing resources within collections
            response = '<?xml version="1.0" encoding="UTF-8"?>\n'
            response += '<D:multistatus xmlns:D="DAV:">\n'

            for vcard_id in self._list_vcards():
                response += "  <D:response>\n"
                response += f"    <D:href>{self.path}{vcard_id}</D:href>\n"
                response += "    <D:propstat>\n"
                response += "      <D:prop>\n"
                response += "        <D:resourcetype/>\n"
                response += "        <D:displayname>{vcard_id}</D:displayname>\n"
                response += "        <D:getcontenttype>text/vcard</D:getcontenttype>\n"
                response += "        <D:getcontentlength>{len(self._read_vcard(vcard_id))}</D:getcontentlength>\n"
                response += '        <D:getetag>"{vcard_id}"</D:getetag>\n'
                response += "        <D:getlastmodified>{}</D:getlastmodified>\n".format(
                    datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
                )
                response += "      </D:prop>\n"
                response += "      <D:status>HTTP/1.1 200 OK</D:status>\n"
                response += "    </D:propstat>\n"
                response += "  </D:response>\n"

            response += "</D:multistatus>"

            self._send_response(
                207,
                headers={"Content-Type": 'application/xml; charset="utf-8"'},
                body=response.encode("utf-8"),
            )
        else:
            self._send_response(400)

    def do_GET(self):
        """Handle GET requests to retrieve a specific vCard."""
        parsed_path = urllib.parse.urlparse(self.path)
        vcard_id = os.path.basename(parsed_path.path)

        if vcard_id:
            vcard_data = self._read_vcard(vcard_id)
            if vcard_data:
                self._send_response(
                    200,
                    headers={
                        "Content-Type": "text/vcard; charset=utf-8",
                        "Content-Length": str(len(vcard_data)),
                    },
                    body=vcard_data,
                )
            else:
                self._send_response(404)
        else:
            self._send_response(400)

    def do_PUT(self):
        """Handle PUT requests to create or update a vCard."""
        parsed_path = urllib.parse.urlparse(self.path)
        vcard_id = os.path.basename(parsed_path.path)

        if vcard_id:
            content_length = int(self.headers["Content-Length"])
            vcard_data = self.rfile.read(content_length)
            self._write_vcard(vcard_id, vcard_data)
            self._send_response(201)
        else:
            self._send_response(400)

    def do_DELETE(self):
        """Handle DELETE requests to remove a vCard."""
        parsed_path = urllib.parse.urlparse(self.path)
        vcard_id = os.path.basename(parsed_path.path)

        if vcard_id:
            if self._delete_vcard(vcard_id):
                self._send_response(204)
            else:
                self._send_response(404)
        else:
            self._send_response(400)


def run(server_class=http.server.HTTPServer, handler_class=CardDAVRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving CardDAV server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
