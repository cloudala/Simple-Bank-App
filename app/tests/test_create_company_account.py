import unittest

from ..KontoFirmowe import Konto_Enterprise

class TestBankTransfers(unittest.TestCase):
    # Konto Enterprise
    company_name = "firma"
    nip = "1234567890"
    
    # Feature 7
    # Account-related tests
    def test_create_enterprise_account(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        self.assertEqual(enterprise_account.name, self.company_name, "Name wasn't saved!")
        self.assertEqual(enterprise_account.nip, self.nip, "Nip wasn't saved!")
        self.assertEqual(enterprise_account.saldo, 0, "Saldo isn't equal to 0!")
    
    def test_nip_with_len_9(self):
        enterprise_account = Konto_Enterprise(self.company_name, "123456789")
        self.assertEqual(enterprise_account.nip, "Incorrect nip!", "Nip that is too short was accepted!")

    def test_nip_with_len_11(self):
        enterprise_account = Konto_Enterprise(self.company_name, "12345678901")
        self.assertEqual(enterprise_account.nip, "Incorrect nip!", "Nip that is too long was accepted!")

    def test_nip_is_empty(self):
        enterprise_account = Konto_Enterprise(self.company_name, "")
        self.assertEqual( enterprise_account.nip, "Incorrect nip!", "Empty nip was accepted!")