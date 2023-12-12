from .Konto import Konto
from datetime import datetime
import requests
import os

class Konto_Enterprise(Konto):
    express_fee = 5

    def __init__(self, name, nip):
        # Setting name
        self.name = name

        # Setting nip
        if len(nip) != 10:
            self.nip = "Incorrect nip!"
        else:
            valid_nip = self.nip_exists(nip)
            if valid_nip:
                self.nip = nip
            else:
                raise ValueError("Nip has to belong to a registered entity!")
        
        # Setting saldo
        self.saldo = 0

        # Setting history
        self.history = []
    
    def take_loan(self, amount):
        if self.is_saldo_valid(amount) and self.pays_zus():
            self.saldo += amount
            return True
        else:
            return False
    
    def is_saldo_valid(self, amount):
        if self.saldo >= amount*2:
            return True
        else:
            return False
    
    def pays_zus(self):
        if -1775 in self.history:
            return True
        else: 
            return False

    @classmethod    
    def nip_exists(self, nip):
        gov_url = os.getenv("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl/")
        today = datetime.today().strftime('%Y-%m-%d')
        nip_response = requests.get(f"{gov_url}api/search/nip/{nip}?date={today}")
        print(f"Sending requests to: {nip_response}")
        if nip_response.status_code == 200:
            return True
        else:
            return False
    
    # Feature 19
    def email_account_history(self, email, SMTPConnection):
        today = datetime.today().strftime('%Y-%m-%d')
        topic = f"Wyciąg z dnia {today}"
        message = f"Historia konta Twojej firmy to: {self.history}"
        receiver = email
        return SMTPConnection.wyslij(topic, message, receiver)