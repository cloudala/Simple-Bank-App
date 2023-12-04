import unittest
from unittest.mock import patch
from ..KontoFirmowe import Konto_Enterprise

@patch("app.KontoFirmowe.Konto_Enterprise.nip_exists")
class TestBankTransfers(unittest.TestCase):
    # Konto Enterprise
    company_name = "firma"
    nip = "1234567890"
    valid_nip = "8461627563"
    invalid_nip = "8461627500"
    
    # Feature 7
    # Account-related tests
    def test_create_enterprise_account(self, nip_exists):
        nip_exists.return_value = True
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        self.assertEqual(enterprise_account.name, self.company_name, "Name wasn't saved!")
        self.assertEqual(enterprise_account.nip, self.nip, "Nip wasn't saved!")
        self.assertEqual(enterprise_account.saldo, 0, "Saldo isn't equal to 0!")
    
    def test_nip_with_len_9(self, nip_exists):
        enterprise_account = Konto_Enterprise(self.company_name, "123456789")
        self.assertEqual(enterprise_account.nip, "Incorrect nip!", "Nip that is too short was accepted!")

    def test_nip_with_len_11(self, nip_exists):
        enterprise_account = Konto_Enterprise(self.company_name, "12345678901")
        self.assertEqual(enterprise_account.nip, "Incorrect nip!", "Nip that is too long was accepted!")

    def test_nip_is_empty(self, nip_exists):
        enterprise_account = Konto_Enterprise(self.company_name, "")
        self.assertEqual( enterprise_account.nip, "Incorrect nip!", "Empty nip was accepted!")

    # Feature 18
    def test_invalid_nip(self, nip_exists):
        nip_exists.return_value = False
        with self.assertRaises(ValueError) as context:
            Konto_Enterprise(self.company_name, self.invalid_nip)
        self.assertTrue("Nip has to belong to a registered entity!" in str(context.exception))