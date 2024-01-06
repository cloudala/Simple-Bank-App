import unittest
from unittest.mock import patch
from ..RejestrKont import Rejestr_Kont

class TestDatabaseIntegration(unittest.TestCase):
    # Konto Personal
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"

    @classmethod
    def setUpClass(cls):
         Rejestr_Kont.accounts = []

    @classmethod
    def tearDownClass(cls):
         Rejestr_Kont.accounts = []

    @patch('app.RejestrKont.Rejestr_Kont.collection')
    def test_load_accounts_from_database(self, mock_collection):
        mock_collection.find.return_value = [{"name": self.name, "surname": self.surname, "pesel": self.pesel, "saldo": 0, "history": []}]
        Rejestr_Kont.load()
        self.assertEqual(len(Rejestr_Kont.accounts), 1)
        self.assertEqual(Rejestr_Kont.accounts[0].name, self.name)
        self.assertEqual(Rejestr_Kont.accounts[0].surname, self.surname)
        self.assertEqual(Rejestr_Kont.accounts[0].pesel, self.pesel)
        self.assertEqual(Rejestr_Kont.accounts[0].saldo, 0)
        self.assertEqual(Rejestr_Kont.accounts[0].history, [])
    
    @patch('app.RejestrKont.Rejestr_Kont.collection')
    def test_save_accounts_to_database(self, mock_collection):
        Rejestr_Kont.save()

        mock_collection.delete_many.assert_called_once_with({})

        mock_collection.insert_one.assert_called_once_with({
            "name": self.name,
            "surname": self.surname,
            "pesel": self.pesel,
            "saldo": 0,
            "history": []
        })