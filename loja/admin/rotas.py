from flask import render_template, request, redirect, session, url_for, flash
from .forms import RegistrationForm
from loja import app, db, bcrypt
from .models import User
import os



@app.route('/')
def home():
    return "Seja bem vindo à nossa loja!"


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(firstname=form.firstname.data, lastname=form.lastname.data,username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        flash('Obrigado por se registrar')
        return redirect(url_for('home'))
    return render_template('admin/registrar.html', form=form, title='Registrar Usuário')

