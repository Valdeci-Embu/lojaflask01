from flask import render_template, request, redirect, session, url_for, flash
from .forms import RegistrationForm, LoginForm
from loja import app, db, bcrypt
from .models import User
import os



@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Faça login para entrar', 'danger')
        return redirect(url_for ('login'))
    return render_template('admin/index.html', title='Início')


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(firstname=form.firstname.data, lastname=form.lastname.data,username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Obrigado, {form.firstname.data} por se registrar', 'success')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title='Registrar Usuário')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Você fez login como {form.email.data}', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash(f'Login inválido', 'success')
    return render_template('admin/login.html', form=form, title='Entrar')