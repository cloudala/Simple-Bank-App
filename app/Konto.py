class Konto:
    express_fee = 0
    
    def incoming_transfer(self, amount):
        if amount > 0:
            self.saldo = self.saldo + amount
        else:
            self.saldo = self.saldo
        return self.saldo
    
    def outgoing_transfer(self, amount):
        if amount > self.saldo or amount <= 0:
            self.saldo = self.saldo
        else:
            self.saldo = self.saldo - amount
        return self.saldo

    def outgoing_express_transfer(self, amount):
        if amount > self.saldo + self.express_fee or amount <= 0:
            self.saldo = self.saldo
        else:
            self.saldo = self.saldo - (amount + self.express_fee)
        return self.saldo

