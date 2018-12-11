## Cijeli Flask projekt predavanja "Autentikacija i autorizacija u Flasku"
### Upute:
* Klonirajte ili preuzmite kod
  * git clone https://github.com/unizd/Oblikovanje-web-stranica
* Uđite u mapu projekta
  * cd 9\Autentikacija\End
* Kreirajte virtualno okruženje
  * python -m venv venv
* Aktivirajte virtualno okruženje
  * venv\Scripts\activate
* Postavite varijable okruženja:
  * set FLASK_APP=main.py
  * set FLASK_DEBUG=1
* Instalirajte sve potrebne ekstenzije i pakete
  * pip install -r requirements.txt
* Pokrenite Flask aplikaciju
  * flask run
  * U pregledniku odite na http://localhost:5000
* Napomena za prijavu
  * Po pokretanju aplikacije prijavite se s nekim od korisnika iz users.json datoteke. Sve zaporke u users.json datoteci su kriptirane, a redom one su: sifra1, sifra2, sifra3, sifra4. Da bi vam autentikacija radila, morate ostaviti app.secret_key isti, u protivnom check_password_hash() metoda neće ispravno raditi.