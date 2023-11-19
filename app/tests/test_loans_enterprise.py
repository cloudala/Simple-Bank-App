import unittest

from ..KontoFirmowe import Konto_Enterprise
from parameterized import parameterized

class TestLoans(unittest.TestCase):
    # Konto Enterprise
    company_name = "firma"
    nip = "1234567890"

    # Feature 13
    def setUp(self):
         self.konto = Konto_Enterprise(self.company_name, self.nip)
    @parameterized.expand([
        (250, [-100, 100], 500, False, 250), 
        (1200, [-100, 100, 200, -50], 500, False, 1200), 
        (1000, [-1775, 100, 200, 50], 500, True, 1500),
        (1200, [-1775, 100, -1775, 10, -60, 30], 500, True, 1700) 
    ])

    def test_loan_system(self, saldo, history, amount, expected_loan_outcome, expected_saldo):
        self.konto.saldo = saldo
        self.konto.history = history
        is_loan_given = self.konto.take_loan(amount)
        self.assertEqual(is_loan_given, expected_loan_outcome, "Incorrect loan feedback!")
        self.assertEqual(self.konto.saldo, expected_saldo, "Incorrect saldo!")