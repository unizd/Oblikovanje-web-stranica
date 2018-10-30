from flask import Flask, render_template, request
from config import Config
import validators
import json

app = Flask(__name__)
app.debug = True

@app.route("/comments", methods=['get', 'post'])
def komentari():
	
	komentari = []
	
	poruka = ''
	
	# Učitavamo komentare iz datoteke
	with open('komentari.json', mode='r', encoding='utf-8') as json_datoteka:
		komentari = json.load(json_datoteka)
		json_datoteka.close()
	
	# Ako je metoda POST onda podatke validiramo i spremamo
	if request.method == 'POST':
		ime = request.form["ime"]
		komentar = request.form["komentar"]
		
		if len(ime)<3 or len(komentar)<3:
			ispravan_unos = False
			poruka = 'Pogrešan unos.'
		else:
			ispravan_unos = True
			poruka = 'Uspješan unos.'
			
		# Zapisujemo komentare u datoteku
		if ispravan_unos:
			with open('komentari.json', mode='w', encoding='utf-8') as json_datoteka:
				komentari.append({"ime": ime, "komentar": komentar})
				json.dump(komentari, json_datoteka)
				json_datoteka.close()
	
	# Prikazujemo podatke
	return render_template("comments.html", komentari=komentari, poruka=poruka)


if __name__ == "__main__":
	app.run()
