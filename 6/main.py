from flask import Flask, render_template, request, redirect
from config import Config
import requests
import json

app = Flask(__name__)
app.debug = True
app.secret_key = b'xen_o7q536_*88^j-)m$pyyp*gmq$()8!p*ral@+k5+_=^jnjd'

@app.route("/")
def index():
	
	# Priprema parametara
	parameters = {'id': Config.userId}
	
	# Poziv REST servisa, HTTP GET
	response = requests.get(Config.usersURL, params=parameters)
	
	# JSON decoder (http://docs.python-requests.org/en/latest/user/quickstart/#json-response-content)
	user = response.json()
	
	name = user[0]['name']
	town = user[0]['address']['city']
	address = user[0]['address']['street']
	company = user[0]['company']['name']
	
	return render_template("index.html", name=name, town=town, address=address, company=company)


@app.route("/postovi")
def postovi():

	# Priprema parametara
	parameters = {'userId': Config.userId}
	
	# Poziv REST servisa, HTTP GET
	response = requests.get(Config.postsURL, params=parameters)
	
	# JSON decoder (http://docs.python-requests.org/en/latest/user/quickstart/#json-response-content)
	posts = response.json()

	return render_template("postovi.html", postovi=posts)


@app.route("/albumi")
def albumi():
	
	# Priprema parametara
	parameters = {'userId': Config.userId}
	
	# Poziv REST servisa, HTTP GET
	response = requests.get(Config.albumsURL, params=parameters)
	
	# JSON decoder (http://docs.python-requests.org/en/latest/user/quickstart/#json-response-content)
	albums = response.json()

	return render_template("albumi.html", albumi=albums)
	
@app.route("/slike/<album_id>")
def slike(album_id):

	# Priprema parametara
	parameters = {'albumId': album_id}
	
	# Poziv REST servisa, HTTP GET
	response = requests.get(Config.photosURL, params=parameters)
	
	# JSON decoder (http://docs.python-requests.org/en/latest/user/quickstart/#json-response-content)
	photos = response.json()

	return render_template("slike.html", slike=photos)


@app.route("/zadaci")
def zadaci():
	return render_template("zadaci.html")


if __name__ == "__main__":
	app.run()