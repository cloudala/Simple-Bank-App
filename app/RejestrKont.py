from .KontoOsobiste import Konto_Personal
from pymongo import MongoClient

class Rejestr_Kont:
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    collection = db['konta']
    accounts = []

    @classmethod
    def add_account(cls, account):
        cls.accounts.append(account)
        

    @classmethod
    def find_account(cls, pesel):
        account = [account for account in cls.accounts if account.pesel == pesel]
        if account:
            return account[0]
        else:
            return None

    @classmethod
    def how_many_accounts(cls):
        return len(cls.accounts)
    
    @classmethod
    def delete_account(cls, account):
        if account:
            cls.accounts.remove(account)

    # Feature 20
    # Load - loads account list to database 
    @classmethod
    def load(cls):
        # Clearing the accounts list
        cls.accounts = []

        # Saving accounts from database to accounts list
        for db_account in cls.collection.find({}):
            # Extracting specific keys ('saldo' and 'history') and keeping the rest
            account = Konto_Personal(db_account["name"], db_account["surname"], db_account["pesel"])
            account.saldo = db_account["saldo"]
            account.history = db_account["history"]
            cls.accounts.append(account)
    
    # Save - saves accounts from database to list
    @classmethod
    def save(cls) :
        # Clearing the database
        cls.collection.delete_many({})
        # Saving accounts from accounts list to database
        for account in cls.accounts:
            cls.collection.insert_one({"name": account.name, "surname": account.surname, "pesel": account.pesel, "saldo": account.saldo, "history": account.history})