import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
from ..KontoOsobiste import Konto_Personal
from ..SMTPConnection import SMTPConnection

class TestSendEmailPersonalAccount(unittest.TestCase):
    # Konto Personal
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"
    email = "test@gmail.com"

    # Email content
    today = datetime.today().strftime('%Y-%m-%d')
    topic = f"Wyciąg z dnia {today}"

    # Feature 19
    def test_send_email_success(self):
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = True)
        account = Konto_Personal(self.name, self.surname, self.pesel)
        account.history = [300, 100, -200]
        send_email = account.email_account_history(self.email, smtp_connector)
        self.assertEqual(send_email, True, "Email wasn't sent correctly!")
        smtp_connector.wyslij.assert_called_once_with(self.topic, f"Twoja historia konta to: {account.history}", self.email)

    def test_send_email_failure(self):
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = False)
        account = Konto_Personal(self.name, self.surname, self.pesel)
        account.history = [300, 100, -200]
        send_email = account.email_account_history(self.email, smtp_connector)
        self.assertEqual(send_email, False, "Email was sent correctly (it wasn't supposed to)!")
        smtp_connector.wyslij.assert_called_once_with(self.topic, f"Twoja historia konta to: {account.history}", self.email)
