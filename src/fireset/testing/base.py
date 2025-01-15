import logging
import unittest

from ..webdav import WebDAVApp


EXAMPLE_VCARD1 = b"""\
BEGIN:VCARD
VERSION:3.0
EMAIL;TYPE=INTERNET:jeffrey@osafoundation.org
EMAIL;TYPE=INTERNET:jeffery@example.org
ORG:Open Source Applications Foundation
FN:Jeffrey Harris
N:Harris;Jeffrey;;;
END:VCARD
"""


class WebTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        logging.disable(logging.WARNING)
        self.addCleanup(logging.disable, logging.NOTSET)

    def makeApp(self, resources, properties):
        class Backend:
            get_resource = resources.get

        app = WebDAVApp(Backend())
        app.register_properties(properties)
        return app
