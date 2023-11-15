import unittest

from ..KontoOsobiste import Konto_Personal
from ..RejestrKont import Rejestr_Kont
# from parameterized import parameterized

class TestRejestr(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"

    # Feature 14
    def setUp(self):
         Rejestr_Kont.accounts = []

    @classmethod
    def setUpClass(cls):
         konto = Konto_Personal(cls.name, cls.surname, cls.pesel)
         Rejestr_Kont.add_account(konto)

    def test_add_account(self):
         konto = Konto_Personal(self.name, self.surname, self.pesel)
         Rejestr_Kont.add_account(konto)
         self.assertEqual()

    def test_find_account(self):
         self.assertEqual()
    
    def test_how_many_accounts(self):
         self.assertEqual()

    @classmethod
    def tearDownClass(cls):
         Rejestr_Kont.accounts = []