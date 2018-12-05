from flask import Flask, request, session, render_template, redirect, url_for, flash, current_app
from flask_bootstrap import Bootstrap
from auth import LoginForm, RegisterForm, User
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from werkzeug.security import check_password_hash
import json
from flask_principal import identity_loaded, Principal, Permission, RoleNeed, identity_changed, Identity, AnonymousIdentity

app = Flask(__name__)
app.secret_key = 'NEKA_ŽVRLJOTINA'
bootstrap = Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

principals = Principal(app)
admin_permission = Permission(RoleNeed('Administracija'))

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(form.email.data)
        if user is not None and check_password_hash(user.password, form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('index')
            identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
            flash('Uspješno ste se prijavili!', category='success')
            return redirect(next)
        flash('Neispravno korisničko ime ili zaporka!', category='warning')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
    identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())

    flash('Odjavili ste se.', category='success')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        User.add(form.email.data, form.password.data)
        flash('Sad se možete prijaviti', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/admin')
@login_required
@admin_permission.require(http_exception=401)
def admin():
    with open('users.json') as datoteka:
            users = json.load(datoteka)
            datoteka.close()
    return render_template('admin.html', users=users)

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if not current_user.is_anonymous:
        if current_user.is_admin:
            identity.provides.add(RoleNeed('Administracija'))

@app.errorhandler(401)
def not_authorised(e):
    return render_template('401.html'), 401

@app.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('index'))
    if current_user.confirm(token):
        # User.confirm(current_user.get_id())
        flash('Vaša prijava je potvrđena. Hvala.', category='success')
    else:
        flash('Link za potvrdu nije ispravan ili je istekao.', category='error')
    return redirect(url_for('index'))