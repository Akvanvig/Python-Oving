"""
	Øving 6
	16.10.2018
	Anders Kvanvig

    Python 3
"""

import sqlite3
from flask import Flask, session, request, g, redirect, url_for, abort, render_template, flash, jsonify, escape
from flask_bootstrap import Bootstrap
import forms

#globale variabler
DATABASE = 'blogg.db'
DEBUG = True
SECRET_KEY = 'test'

#Oppretter og starter appen
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)

#Åpner index-sida og viser nyheter/innlegg
@app.route('/')
def index():
    db = get_db()
    cur = db.execute('SELECT * FROM nyheter ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)


#Åpner nyhetsskjema/Legger inn nyhet/innlegg i databasen
@app.route('/opprett_artikkel', methods=['GET', 'POST'])
def opprett_artikkel():
	form = forms.ArtikkelSkjema(request.form)
	if request.method == 'POST' and form.validate():
		db = get_db()
		db.execute(
			'INSERT INTO nyheter (tittel, nyhet, forfatter) values (?, ?, ?)',
			[request.form['tittel'], request.form['innhold'], request.form['forfatter']]
		)
		db.commit()
		flash('innlegget ble sendt og lagret i databasen')
		return redirect(url_for('index'))
	return render_template('opprett_artikkel.html', form=form)

#Legger inn en ny bruker i databasen
@app.route('/add_bruker', methods=['POST'])
def add_bruker():
    db = get_db()
    db.execute(
        'INSERT INTO nyheter (tittel, nyhet, forfatter) values (?, ?, ?)',
        [request.form['tittel'], request.form['nyhet'], request.form['forfatter']]
    )
    db.commit()
    flash('innlegget ble sendt og lagret i databasen')
    return redirect(url_for('index'))

#Viser innloggingsskjema til bruker, og logger dem inn.
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = forms.InnloggingSkjema(request.form)
	if request.method == 'POST' and form.validate():
		return 'Form Submitted'
	return render_template('login.html', form=form)

#Database-----------------------------------------------------------------------------------------
#Oppretter databasen
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

#Kobler til databasen
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

#Åpner forbindelsen til databasen
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

#Lukker forbindelsen til databasen
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

#Oppstart----------------------------------------------------------------------------------------
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
