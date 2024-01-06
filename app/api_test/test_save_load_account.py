import unittest
import requests

class TestSaveLoadAccount(unittest.TestCase):
    url = "http://127.0.0.1:5000/api/accounts"
    data = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "01310112345",
        "saldo": 0
    }

    @classmethod
    def setUpClass(cls):
        requests.post(cls.url, json=cls.data)

    @classmethod
    def tearDownClass(cls):
        requests.delete(f"{cls.url}/{cls.data['pesel']}")
    
    def test_save_load_account(self):
        # Testing save - saves accounts from accounts list to database
        save_response = requests.patch(f"{self.url}/save")
        self.assertEqual(save_response.status_code, 200)

        # Deleting the account from accounts list
        delete_response = requests.delete(f"{self.url}/{self.data['pesel']}")
        self.assertEqual(delete_response.status_code, 200)
        get_response = requests.get(f"{self.url}/count")
        self.assertEqual(get_response.json(), {"count": 0})

        # Testing load - loads account list from database to accounts list
        load_response = requests.patch(f"{self.url}/load")
        self.assertEqual(load_response.status_code, 200)

        get_response = requests.get(f"{self.url}/{self.data['pesel']}")
        self.assertEqual(get_response.status_code, 200)
        self.assertDictEqual(get_response.json(), self.data)
        