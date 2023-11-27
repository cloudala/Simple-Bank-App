import unittest
import requests

class TestAccountCrud(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"
    url = "http://127.0.0.1:5000/api/accounts"

    def setUp(self):
        requests.post(self.url, json ={
            "name": self.name,
            "surname": self.surname,
            "pesel": self.pesel
        })

    def tearDown(self):
        requests.delete(self.url + "/" + self.pesel)
    
    def test_incoming_transfer(self):
        transfer_response = requests.get(self.url + f"/{self.pesel}/transfer", json = {
            "amount": 500,
            "type": "incoming"
        })
        self.assertEqual(transfer_response.status_code, 200, "Transfer wasn't executed correctly!")
        account_response = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(account_response.status_code, 200, "Account, which received transfer wasn't retrieved correctly!")
        self.assertEqual(account_response.json()["saldo"], 500, "Transfer wasn't executed correctly!")

    def test_outgoing_transfer(self):
        pass