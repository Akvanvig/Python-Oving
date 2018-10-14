"""
	Øving 5
	14.10.2018
	Anders Kvanvig

    Python 3
"""

import sqlite3
from flask import Flask, request, g, redirect, url_for, abort, render_template, flash, jsonify

#globale variabler
DATABASE = 'blogg.db'
DEBUG = True
SECRET_KEY = 'test'

#Oppretter og starter appen
app = Flask(__name__)
app.config.from_object(__name__)

#Leter etter data i databasen og viser de
@app.route('/')
def index():
    db = get_db()
    cur = db.execute('SELECT * FROM nyheter ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)

#Legger inn nye data i databasen
@app.route('/add', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute(
        'INSERT INTO nyheter (tittel, nyhet, forfatter) values (?, ?, ?)',
        [request.form['tittel'], request.form['nyhet'], request.form['forfatter']]
    )
    db.commit()
    flash('innlegget ble sendt og lagret i databasen')
    return redirect(url_for('index'))

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

if __name__ == '__main__':
    init_db()
    app.run()
