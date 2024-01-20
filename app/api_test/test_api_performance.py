import unittest
import requests

class TestApiPerformance(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "01310112345"

    def setUp(self):
        self.url = "http://127.0.0.1:5000/api/accounts"

    def test_post_delete_100_accounts(self):
        for i in range(0, 100): 
            post_response = requests.post(self.url, json = {
                "name": self.name,
                "surname": self.surname,
                "pesel": self.pesel
            }, timeout=2)
            self.assertEqual(post_response.status_code, 201, "Account wasn't created correctly!")
            delete_response = requests.delete(self.url + "/01310112345", timeout=2)
            self.assertEqual(delete_response.status_code, 200, "Account wasn't deleted correctly!")