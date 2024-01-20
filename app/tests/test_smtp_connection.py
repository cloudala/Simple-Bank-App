import unittest
from ..SMTPConnection import SMTPConnection

class TestSMTPConnection(unittest.TestCase):
    def test_smtp_connection(self):
        smtp_connector = SMTPConnection()
        self.assertFalse(smtp_connector.wyslij("Content", "Recipient"), "Default value returned by SMTP Connection isn't false!")