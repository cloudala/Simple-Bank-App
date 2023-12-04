import unittest
from ..KontoOsobiste import Konto_Personal

class TestBankTransfers(unittest.TestCase):
    # Konto
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"
    promo_code = "PROM_XYZ"

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
    
    # Feature 11
    # Konto Personal
    def test_incoming_transfer_registration(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel, self.promo_code)
        konto.incoming_transfer(50)
        self.assertEqual(konto.history, [50], "Incoming transfer amount hasn't been registered in history!")

    def test_outgoing_transfer_registration(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel, self.promo_code)
        konto.outgoing_transfer(25)
        self.assertEqual(konto.history, [-25], "Outgoing transfer amount hasn't been registered in history!")

    def test_outgoing_express_transfer_registration(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel, self.promo_code)
        konto.outgoing_express_transfer(25)
        self.assertEqual(konto.history, [-25, -1], "Outgoing express transfer amount and/or fee hasn't been registered in history!")