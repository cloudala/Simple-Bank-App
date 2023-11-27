from flask import Flask, request, jsonify
from app.RejestrKont import Rejestr_Kont
from app.KontoOsobiste import Konto_Personal

app = Flask(__name__)

# Creating an account
@app.route("/api/accounts", methods=['POST'])
def stworz_konto():
    dane = request.json
    print(f"Request to create account with data: {dane}")
    accountExists = Rejestr_Kont.find_account(dane["pesel"])
    if accountExists is None:
        konto = Konto_Personal(dane["name"], dane["surname"], dane["pesel"])
        Rejestr_Kont.add_account(konto)
        return jsonify({"message": "Account created!"}), 201
    else:
        return jsonify({"message": "Account already exists!"}), 409

# Getting number of accounts
@app.route("/api/accounts/count", methods=['GET'])
def ile_kont():
    number = Rejestr_Kont.how_many_accounts()
    return jsonify({"count": number }), 200

# Getting account by pesel
@app.route("/api/accounts/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    konto = Rejestr_Kont.find_account(pesel)
    if konto:
        return jsonify(
            {"name": konto.name, 
             "surname": konto.surname, 
             "pesel": konto.pesel
             }), 200
    else:
        return jsonify({"message": "Account not found!"}), 404

# Updating account with pesel
@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def zmien_konto(pesel):
    dane = request.json
    print(f"Request to change account data")
    konto = Rejestr_Kont.find_account(pesel)
    account_fields = ["name", "surname", "pesel", "saldo"]
    if konto:
        for account_field in account_fields:
            if account_field in dane:
                setattr(konto, account_field, dane[account_field])
        return jsonify({"name": konto.name, "surname": konto.surname, "pesel": konto.pesel, "saldo": konto.saldo}), 200
    else:
         return jsonify({"message": "Account not found!"}), 404

# Deleting account with pesel
@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def usun_konto_z_peselem(pesel):
    konto = Rejestr_Kont.find_account(pesel)
    if konto:
        Rejestr_Kont.delete_account(konto)
        return jsonify(
            {"message": "Account deleted successfully!"}), 200
    else:
        return jsonify({"message": "Account not found!"}), 404

# Feature 17 -> API transfers
@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def send_transfer(pesel):
    dane = request.json
    print(f"Request to send transfer with data: {dane}")
    accountExists = Rejestr_Kont.find_account(pesel)
    if accountExists is None:
        return jsonify({"message": "Account doesn't exist! Transfer can't be executed!"}), 404
    else:
        if (dane["type"] == "outgoing"):
            transferAmount = -1*dane["amount"]
            accountExists.outgoing_transfer(transferAmount)
        else:
            transferAmount = dane["amount"]
            accountExists.incoming_transfer(transferAmount)
    return jsonify({"message": f"Transfer accepted for execution! {transferAmount}"}), 200
