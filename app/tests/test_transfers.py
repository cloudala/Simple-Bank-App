import unittest

from ..KontoOsobiste import Konto_Personal
from ..KontoFirmowe import Konto_Enterprise

class TestBankTransfers(unittest.TestCase):
    # Konto
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"
    promo_code = "PROM_XYZ"

    # Konto Enterprise
    company_name = "firma"
    nip = "1234567890"

    # Feature 6
    def test_incoming_transfer(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel, self.promo_code)
        konto.incoming_transfer(50)
        self.assertEqual(konto.saldo, 100, "Saldo hasn't increased despite incoming transfer!")
    
    def test_incoming_transfer_invalid_amount(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel, self.promo_code)
        konto.incoming_transfer(-50)
        self.assertEqual(konto.saldo, 50, "Saldo has changed despite invalid amount!")

    def test_outgoing_transfer_sufficient_balance(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel, self.promo_code)
        konto.outgoing_transfer(25)
        self.assertEqual(konto.saldo, 25, "Saldo hasn't decreased despite outgoing transfer!")
    
    def test_outgoing_transfer_insufficient_balance(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel)
        konto.outgoing_transfer(25)
        self.assertEqual(konto.saldo, 0, "Saldo has decresed despite insufficient funds to make the transfer!")

    def test_outgoing_transfer_invalid_amount(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel, self.promo_code)
        konto.outgoing_transfer(-50)
        self.assertEqual(konto.saldo, 50, "Saldo has changed despite invalid amount!")
        
    # Feature 7
    # Transfer-related tests
    def test_enterprise_incoming_transfer(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        enterprise_account.incoming_transfer(100)
        self.assertEqual(enterprise_account.saldo, 100, "Saldo hasn't increased despite incoming transfer!")
    
    def test_enterprise_incoming_transfer_invalid_amount(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        enterprise_account.incoming_transfer(-100)
        self.assertEqual(enterprise_account.saldo, 0, "Saldo has changed despite invalid amount!")

    def test_enterprise_outgoing_transfer_sufficient_balance(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        # Transferring some money so that we have sufficient funds
        enterprise_account.incoming_transfer(100)
        enterprise_account.outgoing_transfer(25)
        self.assertEqual(enterprise_account.saldo, 75, "Saldo hasn't decreased despite outgoing transfer!")
    
    def test_enterprise_outgoing_transfer_insufficient_balance(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        enterprise_account.outgoing_transfer(25)
        self.assertEqual(enterprise_account.saldo, 0, "Saldo has decresed despite insufficient funds to make the transfer!")
    
    def test_enterprise_outgoing_transfer_invalid_amount(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        enterprise_account.outgoing_transfer(-100)
        self.assertEqual(enterprise_account.saldo, 0, "Saldo has changed despite invalid amount!")

    # Feature 8
    # Konto --> transfer fee = 1zł
    def test_outgoing_express_transfer_sufficient_balance(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel, self.promo_code)
        konto.outgoing_express_transfer(25)
        self.assertEqual(konto.saldo, 24, "Incorrect saldo after express transfer!")
    
    def test_outgoing_express_transfer_balance_enables_transaction(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel, self.promo_code)
        konto.outgoing_express_transfer(49.5)
        self.assertEqual(konto.saldo, -0.5, "Incorrect saldo after express transfer!")
    
    def test_outgoing_express_transfer_balance_equal_to_transaction_amount(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel, self.promo_code)
        konto.outgoing_express_transfer(50)
        self.assertEqual(konto.saldo, -1, "Incorrect saldo after express transfer!")
    
    def test_outgoing_express_transfer_insufficient_balance(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel)
        konto.outgoing_express_transfer(50)
        self.assertEqual(konto.saldo, 0, "Incorrect saldo after express transfer!")
    
    def test_outgoing_express_transfer_invalid_amount(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel)
        konto.outgoing_express_transfer(-50)
        self.assertEqual(konto.saldo, 0, "Incorrect saldo after express transfer!")

    # Konto Enterprise --> transfer fee = 5zł
    def test_enterprise_outgoing_express_transfer_sufficient_balance(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        # Transferring some money so that we have sufficient funds
        enterprise_account.incoming_transfer(100)
        enterprise_account.outgoing_express_transfer(50)
        self.assertEqual(enterprise_account.saldo, 45, "Incorrect saldo after express transfer!")
    
    def test_enterprise_outgoing_express_transfer_balance_enables_transaction(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        # Transferring some money so that we have sufficient funds
        enterprise_account.incoming_transfer(100)
        enterprise_account.outgoing_express_transfer(97)
        self.assertEqual(enterprise_account.saldo, -2, "Incorrect saldo after express transfer!")
    
    def test_enterprise_outgoing_express_transfer_balance_equal_to_transaction_amount(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        # Transferring some money so that we have sufficient funds
        enterprise_account.incoming_transfer(100)
        enterprise_account.outgoing_express_transfer(100)
        self.assertEqual(enterprise_account.saldo, -5, "Incorrect saldo after express transfer!")
    
    def test_enterprise_outgoing_express_transfer_insufficient_balance(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        enterprise_account.outgoing_express_transfer(50)
        self.assertEqual(enterprise_account.saldo, 0, "Incorrect saldo after express transfer!")
    
    def test_enterprise_outgoing_express_transfer_invalid_amount(self):
        enterprise_account = Konto_Enterprise(self.company_name, self.nip)
        enterprise_account.outgoing_express_transfer(-50)
        self.assertEqual(enterprise_account.saldo, 0, "Incorrect saldo after express transfer!")