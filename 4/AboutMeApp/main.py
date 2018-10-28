from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():

	ime_i_prezime = Config.name + ' ' + Config.surname
	
	return render_template("index.html",
						   name = ime_i_prezime)

@app.route("/education")
def obrazovanje():
	return render_template("education.html")
	
	
if __name__ == "__main__":
	app.run()
