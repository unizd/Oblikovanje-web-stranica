from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	ime_i_prezime = Config.name + ' ' + Config.surname
	return render_template("index.html", name = ime_i_prezime)

@app.route("/education")
def obrazovanje():
	return render_template("education.html")

@app.route("/bankAccount")
def bankovni_racun():
	ime_banke = Config.banka
	broj_racuna = Config.iban	
	return render_template("bankAccount.html", banka=ime_banke, iban=broj_racuna)
	
	
if __name__ == "__main__":
	app.run()
