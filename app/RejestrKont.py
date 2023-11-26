class Rejestr_Kont:
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