from flask import Flask, request, jsonify
from app.RejestrKont import Rejestr_Kont
from app.KontoOsobiste import Konto_Personal

app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])
def stworz_konto():
    dane = request.json
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto_Personal(dane["imie"], dane["nazwisko"], dane["pesel"])
    Rejestr_Kont.add_account(konto)
    return jsonify({"message": "Konto stworzone"}), 201

@app.route("/api/accounts/count", methods=['GET'])
def ile_kont():
    number = Rejestr_Kont.how_many_accounts()
    return jsonify({"count": number }), 200



@app.route("/api/accounts/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    konto = Rejestr_Kont.find_account(pesel)
    if konto != None:
        return jsonify({"name": "konto.imie", "inne_dane": "uzupełnij"}), 200
    else:
        return jsonify({"message": "Account not found!"}), 404