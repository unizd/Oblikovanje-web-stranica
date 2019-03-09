# p7-flask-openweathermap-api
Flask aplikacija odrađena na SIT predavanju 22.11.2018.

Napomene:
1. U liniji 19. stavite APPID koji ste dobili prilikom registracije na openweathermap servis
2. Kreirajte i aktivirajte virtualno okruženje:
    python -m venv venv
    .\venv\Scripts\Activate.ps1 (ili activate.bat)
3. Prije pokretanja povucite potrebne pakete naredbom "pip install -r requirements.txt"
4. Postavite ENV varijable:
    $env:FLASK_APP = "main.py" (ili "set FLASK_APP=main.py")
	$env:FLASK_DEBUG = 1 (ili "set FLASK_DEBUG=1)
5. Pokrenite aplikaciju: "flask run"
6. Primijetite da je na View funkcijama postavljeno "keširanje" od 10 sekundi, pa promjene u kodu neće biti odmah vidljive ako ste mijenjati "template".


