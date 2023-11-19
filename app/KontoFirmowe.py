from .Konto import Konto

class Konto_Enterprise(Konto):
    express_fee = 5

    def __init__(self, name, nip):
        # Setting name
        self.name = name

        # Setting nip
        if len(nip) != 10:
            self.nip = "Incorrect nip!"
        else:
            self.nip = nip
        
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