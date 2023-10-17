import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"

    # Feature 1 & Feature 2
    def test_creating_account(self):
        first_account = Konto(self.name, self.surname, self.pesel)
        self.assertEqual(first_account.name, self.name, "Name wasn't saved!")
        self.assertEqual(first_account.surname, self.surname, "Surname wasn't saved!")
        self.assertEqual(first_account.saldo, 0, "Saldo isn't equal to 0!")
        self.assertEqual(first_account.pesel, self.pesel, "Pesel wasn't given!")

    # Feature 3
    def test_pesel_with_len_10(self):
        konto = Konto(self.name, self.surname, "1234567890")
        self.assertEqual(konto.pesel, "Incorrect pesel!", "Pesel that is too short was accepted!")

    def test_pesel_with_len_12(self):
        konto = Konto(self.name, self.surname, "123456789012")
        self.assertEqual(konto.pesel, "Incorrect pesel!", "Pesel that is too long was accepted!")

    def test_pesel_is_empty(self):
        konto = Konto(self.name, self.surname, "")
        self.assertEqual(konto.pesel, "Incorrect pesel!", "Empty pesel was accepted!")

    # Feature 4
    def test_without_promo_code(self):
        konto = Konto(self.name, self.surname, self.pesel)
        self.assertEqual(konto.saldo, 0, "Saldo greater than 0 despite no promo code usage!")

    def test_with_promo_code(self):
        konto = Konto(self.name, self.surname, self.pesel, "PROM_ALA")
        self.assertEqual(konto.saldo, 50, "Saldo is not 50 despite promo code usage!")

    def test_with_other_promo_code(self):
        konto = Konto(self.name, self.surname, self.pesel, "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "Saldo is not 50 despite promo code usage!")

    def test_with_invalid_promo_code(self):
        konto = Konto(self.name, self.surname, self.pesel, "PROM_XYZM")
        self.assertEqual(konto.saldo, 0, "Saldo greater than 0 despite invalid promo code usage!")

    # Feature 5
    def test_promo_year_1959(self):
        konto = Konto(self.name, self.surname, "59092312345", "PROM_XYZ")
        self.assertEqual(konto.saldo, 0, "Saldo greater than 0 despite user not being eligible!")

    def test_promo_year_1961(self):
        konto = Konto(self.name, self.surname, "61092312345", "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "Saldo is not 50 despite user being eligible!")

    def test_promo_year_1960(self):
        konto = Konto(self.name, self.surname, "60092312345", "PROM_XYZ")
        self.assertEqual(konto.saldo, 0, "Saldo greater than 0 despite user not being eligible!")

    def test_promo_year_2001(self):
        konto = Konto(self.name, self.surname, self.pesel, "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "Saldo is not 50 despite user being eligible!")

    def test_promo_year_2001_wrong_promo_code(self):
        konto = Konto(self.name, self.surname, self.pesel, "PROM_XYZa")
        self.assertEqual(konto.saldo, 0, "Saldo greater than 0 despite invalid promo code usage!")

    def test_promo_year_2001_wrong_pesel(self):
        konto = Konto(self.name, self.surname, "013101123452", "PROM_XYZ")
        self.assertEqual(konto.saldo, 0, "Saldo greater than 0 despite invalid pesel!")
