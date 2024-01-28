from flask import request, render_template, redirect, url_for, flash
from loja import app, db
from .models import Marcas, Categoria

@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
    if request.method == "POST":
        getmarca = request.form.get('marca')
        marca = Marcas(name=getmarca)
        db.session.add(marca)
        db.session.commit()
        flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
        return redirect(url_for('addmarca'))
    return render_template('produtos/addmarca.html', marcas='marcas')