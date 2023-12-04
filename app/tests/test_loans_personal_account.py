import unittest

from ..KontoOsobiste import Konto_Personal
from parameterized import parameterized

class TestLoans(unittest.TestCase):
    # Konto
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"
    promo_code = "PROM_XYZ"

    # Feature 13
    def setUp(self):
         self.konto = Konto_Personal(self.name, self.surname, self.pesel)
    @parameterized.expand([
        ([-100, 100], 500, False, 0), 
        ([-100, 100, 200, -50], 500, False, 0), 
        ([-100, 100, 200, 10, 20, -30], 500, False, 0), 
        ([-100, 100, 200, -50, -60, 30], 500, False, 0),
        ([-100, 100, 200, 50], 500, True, 500),
        ([-100, 100, 500, 10, -60, 30], 500, True, 500), 
        ([100, 100, 500, 10, 60, 30], 500, True, 500)
    ])

    def test_loan_system(self, history, amount, expected_loan_outcome, expected_saldo):
        self.konto.history = history
        is_loan_given = self.konto.take_loan(amount)
        self.assertEqual(is_loan_given, expected_loan_outcome, "Incorrect loan feedback!")
        self.assertEqual(self.konto.saldo, expected_saldo, "Incorrect saldo!")