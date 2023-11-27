import unittest
from parameterized import parameterized
from ..KontoOsobiste import Konto_Personal
from ..RejestrKont import Rejestr_Kont

class TestRejestr(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"

    # Feature 14
    def setUp(self):
         self.konto = Konto_Personal(self.name, self.surname, self.pesel)

    @classmethod
    def tearDownClass(cls):
         Rejestr_Kont.accounts = []
         
    @parameterized.expand([
         ("name1", "surname1", "12345678901", 1),
         ("name2", "surname2", "12345678902", 2),
         ("name3", "surname3", "12345678903", 3)
    ])
    def test_add_account(self, name, surname, pesel, howManyAccountsNow):
         konto = Konto_Personal(name, surname, pesel)
         Rejestr_Kont.add_account(konto)
         self.assertEqual(Rejestr_Kont.how_many_accounts(), howManyAccountsNow, "Number of accounts is not calculated correctly!")

    def test_find_account(self):
         Rejestr_Kont.add_account(self.konto)
         foundAccount = Rejestr_Kont.find_account(self.pesel)
         self.assertEqual(foundAccount, self.konto, "The account wasn't correctly found!")

    def test_find_nonexistent_account(self):
         foundAccount = Rejestr_Kont.find_account('01310112343')
         self.assertEqual(foundAccount, None, "The account wasn't correctly found!")
     
    def test_delete_account(self):
         beginning_number_of_accounts = Rejestr_Kont.how_many_accounts()
         Rejestr_Kont.add_account(self.konto)
         Rejestr_Kont.delete_account(self.konto)
         end_number_of_accounts = Rejestr_Kont.how_many_accounts()
         self.assertEqual(beginning_number_of_accounts, end_number_of_accounts, "The account wasn't deleted correctly!")