import unittest

from ..KontoOsobiste import Konto_Personal

class TestLoans(unittest.TestCase):
    # Konto
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"
    promo_code = "PROM_XYZ"

    # Feature 13
    # Konto Personal
    # Expecting False -> loan not given
    def test_one(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel)
        konto.history = [-100, 100]
        loan_given = konto.take_loan(500)
        self.assertFalse(loan_given)
    
    def test_two(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel)
        konto.history = [-100, 100, 200, -50, -60, 30]
        loan_given = konto.take_loan(500)
        self.assertFalse(loan_given)
    
    # Expecting True -> loan given
    def test_three(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel)
        konto.history = [-100, 100, 200, 50, 60, 30]
        loan_given = konto.take_loan(500)
        self.assertTrue(loan_given)
    
    def test_four(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel)
        konto.history = [-100, -100, 500, 10, 60, 30]
        loan_given = konto.take_loan(500)
        self.assertTrue(loan_given)
    
    def test_five(self):
        konto = Konto_Personal(self.name, self.surname, self.pesel)
        konto.history = [100, 100, 500, 10, 60, 30]
        loan_given = konto.take_loan(500)
        self.assertTrue(loan_given)