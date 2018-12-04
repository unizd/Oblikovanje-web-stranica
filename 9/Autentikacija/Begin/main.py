from flask import Flask

app = Flask(__name__)
app.secret_key = 'NEKA_ŽVRLJOTINA'

@app.route('/')
def index():
    return '<h1>Hello World</h1>'