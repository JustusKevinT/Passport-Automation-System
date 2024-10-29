from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.data_models import User
from werkzeug.security import generate_password_hash, check_password_hash
from website import db
from flask_login import login_user, login_required, logout_user, current_user

Login = Blueprint('Login',__name__)

@Login.route('/CreateLogin', methods=['GET','POST'])
def CreateLogin():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exist.',category='error')
        elif len(username) < 4:
            flash('Username must be greater than 4 characters.',category='error')
        elif len(email) < 1:
            flash('Email must be greater than 1 character.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters.',category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.',category='error')
        else:
            new_user = User(username=username,email=email,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!',category='success')
            return redirect(url_for('Registration.add'))
    return render_template("CreateLogin.html", user=current_user)

@Login.route('/Logout')
@login_required
def Logout():
    logout_user()
    return redirect(url_for('Login.Signin'))

@Login.route('/Signin', methods=['GET','POST'])
def Signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Signed in successfully!',category='success')
                login_user(user, remember=True)
                return redirect(url_for('Registration.add'))
            else:
                flash('Incorrect password or username.',category='error')
        else:
            flash('User does not exist.',category='error')
    return render_template("Signin.html",user = current_user)
