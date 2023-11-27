import unittest
import requests

class TestAccountCrud(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"

    def setUp(self):
        self.url = "http://127.0.0.1:5000/api/accounts"

    def test_1_post_account(self):
        response = requests.post(self.url, json = {
            "name": self.name,
            "surname": self.surname,
            "pesel": self.pesel
        })
        self.assertEqual(response.status_code, 201, "Account wasn't created correctly!")
    
    def test_2_get_account(self):
        response = requests.get(self.url + "/01310112345")
        self.assertEqual(response.status_code, 200, "Account wasn't found correctly!")
        expected_data = {"name": self.name, "surname": self.surname, "pesel": self.pesel}
        received_data = response.json()
        self.assertDictEqual(expected_data, received_data, "Account wasn't found correctly!")

    def test_3_get_nonexistent_account(self):
        response = requests.get(self.url + "/01310112343")
        self.assertEqual(response.status_code, 404, "Account wasn't found correctly!")
    
    def test_4_count_accounts(self):
        response = requests.get(self.url + "/count")
        self.assertEqual(response.status_code, 200, "Number of accounts wasn't counted correctly!")
        self.assertEqual({"count": 1}, response.json(), "Number of accounts wasn't counted correctly!")
    
    def test_5_patch_account(self):
        response = requests.patch(self.url + "/01310112345", json = {
            "name": "Jan",
            "saldo": 100,
        })
        self.assertEqual(response.status_code, 200, "Account wasn't updated correctly!")
        expected_data = {"name": "Jan", "surname": self.surname, "pesel": self.pesel, "saldo": 100}
        received_data = response.json()
        self.assertDictEqual(expected_data, received_data, "Account wasn't updated correctly!")

    def test_6_patch_nonexistent_account(self):
        response = requests.patch(self.url + "/01310112343", json = {
            "name": "Jan",
            "saldo": 100,
        })
        self.assertEqual(response.status_code, 404, "Account wasn't updated correctly!")

    def test_7_delete_account(self):
        response = requests.delete(self.url + "/01310112345")
        self.assertEqual(response.status_code, 200, "Account wasn't deleted correctly!")
    
    def test_8_delete_account(self):
        response = requests.delete(self.url + "/01310112343")
        self.assertEqual(response.status_code, 404, "Account wasn't deleted correctly!")
    
    # Feature 16 - test duplicate account
    def test_9_post_duplicate_account(self):
        requests.post(self.url, json = {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "23456789012"
        })
        response = requests.post(self.url, json = {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "23456789012"
        })
        self.assertEqual(response.status_code, 409, "Duplicate account was added!")
    