class Konto:
    express_fee = 0
    
    def incoming_transfer(self, amount):
        if amount > 0:
            self.saldo = self.saldo + amount
            self.history.append(amount)
        else:
            self.saldo = self.saldo
        return self.saldo
    
    def outgoing_transfer(self, amount):
        if amount > self.saldo or amount <= 0:
            self.saldo = self.saldo
        else:
            self.saldo = self.saldo - amount
            amount_to_record = 0 - amount
            self.history.append(amount_to_record)
        return self.saldo

    def outgoing_express_transfer(self, amount):
        if amount > self.saldo + self.express_fee or amount <= 0:
            self.saldo = self.saldo
        else:
            self.saldo = self.saldo - (amount + self.express_fee)
            amount_to_record = 0 - amount
            fee_to_record = 0 - self.express_fee
            self.history.append(amount_to_record)
            self.history.append(fee_to_record)
        return self.saldo

