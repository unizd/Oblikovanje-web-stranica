from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_login import UserMixin
import json
from werkzeug.security import generate_password_hash

class LoginForm(FlaskForm):
    email = TextField('E-mail', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Zaporka', validators=[DataRequired()])
    remember_me = BooleanField('Ostani prijavljen')
    submit = SubmitField('Prijava')

class RegisterForm(FlaskForm):
    email = TextField('E-mail', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Zaporka', validators=[
        DataRequired(), EqualTo('password2', message='Zaporke moraju biti jednake.')])
    password2 = PasswordField('Potvrdi zaporku', validators=[DataRequired()])
    submit = SubmitField('Registracija')

class User(UserMixin):
    def __init__(self, id):
        with open('users.json') as datoteka:
            self.USERS = json.load(datoteka)
            datoteka.close()

        if not id in self.USERS:
            raise UserNotFoundError()
        self.id = id
        self.password = self.USERS[id]
        self.is_admin = self.check_if_admin(id)
         
    @classmethod
    def get(self_class, id):
        try:
            return self_class(id)
        except UserNotFoundError:
            return None

    @staticmethod
    def add(id, password):
        entries = {}
        with open('users.json', mode='r') as datoteka:
            entries = json.load(datoteka)
            datoteka.close()
        entries[id] = generate_password_hash(password)
        with open('users.json', mode='w') as datoteka:
            json.dump(entries, datoteka)

    def check_if_admin(self, id):
        with open('roles.json') as datoteka:
            roles = json.load(datoteka)
            datoteka.close()
            if not id in roles:
                return False
            elif 'Administrator' in roles[id]:
                return True
            return False

class UserNotFoundError(Exception):
    pass
