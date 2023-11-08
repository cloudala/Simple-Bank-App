from .Konto import Konto

class Konto_Personal(Konto):
    express_fee = 1

    def __init__(self, name, surname, pesel, promo_code = None):
        # Setting name and surname
        self.name = name
        self.surname = surname

        # Setting pesel
        if len(pesel) != 11:
            self.pesel = "Incorrect pesel!"
        else:
            self.pesel = pesel
        
        # Setting saldo
        birth_year = self.determine_birth_year(self.pesel)
        if self.is_promo_code_correct(promo_code) and self.does_promo_apply(birth_year):
            self.saldo = 50
        else:
            self.saldo = 0
        
        # Setting history
        self.history = []

    def is_promo_code_correct(self, promo_code):
        if promo_code is not None:
            if promo_code.startswith("PROM_") and len(promo_code) == 8:
                return True
            else:
                return False
    
    def determine_birth_year(self, pesel):
        if pesel == "Incorrect pesel!":
            return None
        else:
            pesel_birth_year = int(pesel[0:2])
            pesel_birth_month = int(pesel[2:4])

            if pesel_birth_month > 12:
                birth_year = 2000 + pesel_birth_year
            else:
                birth_year = 1900 + pesel_birth_year
            return birth_year
            
    def does_promo_apply(self, birth_year):
        if birth_year is not None and birth_year > 1960:
            return True
        else:
            return False
    
    def take_loan(self, amount):
        if len(self.history) < 3:
            return False

        last_three_transactions = self.history[-3:]
        last_five_transactions = self.history[-5:]

        if (all(value > 0 for value in last_three_transactions)):
            self.saldo += amount
            return True
        elif (sum(last_five_transactions) > amount):
            self.saldo += amount
            return True
        else:
            return False