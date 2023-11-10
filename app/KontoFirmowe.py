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