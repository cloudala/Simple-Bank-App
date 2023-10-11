import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został podany!")

    def test_pesel_with_len_10(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za krótki pesel został przyjęty za prawidłowy!")

    def test_pesel_with_len_12(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Za długi pesel został przyjęty za prawidłowy!")

    def test_empty_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Pusty pesel został przyjęty za prawidłowy!")

    def without_promo_code(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890")
        self.assertEqual(konto.saldo, 0, "Saldo greater than 0 despite no promo code usage!")

    def with_promo_code(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890", "PROMO_ALA")
        self.assertEqual(konto.saldo, 50, "Saldo is not 50 despite promo code usage!")

    def with_other_promo_code(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890", "PROMO_XYZ")
        self.assertEqual(konto.saldo, 50, "Saldo greater than 0 despite invalid promo code usage!")

    def with_invalid_promo_code(self):
        konto = Konto(self.imie, self.nazwisko, "1234567890", "PROMO_XYZM")
        self.assertEqual(konto.saldo, 0, "Saldo greater than 0 despite invalid promo code usage!")

    def test_promo_year_59(self):
        pass
    def test_promo_year_61(self):
        pass
    def test_promo_year_60(self):
        pass
    def test_promo_year_2001(self):
        pass
    def test_promo_year_2001_wrong_promo_code(self):
        pass
    def test_promo_year_2001_wrong_pesel(self):
        pass
