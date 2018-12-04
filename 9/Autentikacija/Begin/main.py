from flask import Flask, request, session, render_template, redirect, url_for, flash, current_app
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'NEKA_ŽVRLJOTINA'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secret')
def secret():
    return render_template('secret.html')