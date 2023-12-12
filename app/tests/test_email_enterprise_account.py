import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
from ..KontoFirmowe import Konto_Enterprise
from ..SMTPConnection import SMTPConnection

@patch("app.KontoFirmowe.Konto_Enterprise.nip_exists")
class TestSendEmailEnterpriseAccount(unittest.TestCase):
    # Konto Enterprise
    company_name = "firma"
    nip = "1234567890"
    valid_nip = "8461627563"
    email = "test@gmail.com"

    # Email content
    today = datetime.today().strftime('%Y-%m-%d')
    topic = f"Wyciąg z dnia {today}"
    
    # Feature 19
    def test_send_email_success(self, nip_exists):
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = True)
        nip_exists.return_value = True
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        enterprise_account.history = [300, 100, -200]
        send_email = enterprise_account.email_account_history(self.email, smtp_connector)
        self.assertEqual(send_email, True, "Email wasn't sent correctly!")
        smtp_connector.wyslij.assert_called_once_with(self.topic, f"Historia konta Twojej firmy to: {enterprise_account.history}", self.email)

    def test_send_email_failure(self, nip_exists):
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = False)
        nip_exists.return_value = True
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        enterprise_account.history = [300, 100, -200]
        send_email = enterprise_account.email_account_history(self.email, smtp_connector)
        self.assertEqual(send_email, False, "Email wasn't sent correctly!")
        smtp_connector.wyslij.assert_called_once_with(self.topic, f"Historia konta Twojej firmy to: {enterprise_account.history}", self.email)
        