import unittest
from datetime import datetime
from unittest.mock import patch, Mock
from ..KontoFirmowe import Konto_Enterprise

class TestNipExists(unittest.TestCase):
    @patch('app.KontoFirmowe.requests.get')
    def test_nip_exists_valid_nip(self, mock_requests_get):
        # Getting today's date
        today = datetime.today().strftime('%Y-%m-%d')

        # Set up the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response

        # Call the method with a mock valid NIP
        with patch('app.KontoFirmowe.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            result = Konto_Enterprise.nip_exists("8461627563")

        # Checking that nip_exists returned True
        self.assertTrue(result)

        # Verifying that requests.get was called with the expected URL
        expected_url = f"https://wl-test.mf.gov.pl/api/search/nip/8461627563?date={today}"
        mock_get.assert_called_once_with(expected_url)
    
    @patch('app.KontoFirmowe.requests.get')
    def test_nip_exists_invalid_nip(self, mock_requests_get):
        # Getting today's date
        today = datetime.today().strftime('%Y-%m-%d')

        # Set up the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response

        # Call the method with a mock invalid NIP
        with patch('app.KontoFirmowe.requests.get') as mock_get:
            mock_get.return_value.status_code = 400
            result = Konto_Enterprise.nip_exists("8461627500")

        # Checking that nip_exists returned False
        self.assertFalse(result)

        # Verifying that requests.get was called with the expected URL
        expected_url = f"https://wl-test.mf.gov.pl/api/search/nip/8461627500?date={today}"
        mock_get.assert_called_once_with(expected_url)