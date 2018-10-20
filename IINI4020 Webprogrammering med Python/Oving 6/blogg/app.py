"""
        Øving 6
        19.10.2018
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
@app.route('/', methods=['GET', 'POST'])
def index():
        db = get_db()
        cur = db.execute('SELECT n.id AS id, n.tittel AS tittel, n.nyhet AS nyhet, b.navn AS forfatter FROM nyheter n JOIN brukere b ON n.forfatter_id = b.id ORDER BY n.id DESC')
        entries = cur.fetchall()
        cur = db.execute('SELECT * FROM brukere')
        res = cur.fetchall()
        return render_template('index.html',entries=entries,rader=res)


#Åpner nyhetsskjema/Legger inn nyhet/innlegg i databasen
@app.route('/opprett_artikkel', methods=['GET', 'POST'])
def opprett_artikkel():
        if 'brukernavn' not in session:
                return redirect(url_for('login'))
        form = forms.ArtikkelSkjema(request.form)
        if request.method == 'POST' and form.validate():
                db = get_db()
                cur = db.execute('SELECT id FROM brukere WHERE navn = ? AND passord = ?', [session['brukernavn'], session['passord']])
                rad = cur.fetchone()[0]
                db.execute(
                        'INSERT INTO nyheter (tittel, nyhet, forfatter_id) values (?, ?, ?)',
                        [request.form['tittel'], request.form['innhold'], rad]
                )
                db.commit()
                flash('innlegget ble sendt og lagret i databasen')
                return redirect(url_for('index'))
        return render_template('opprett_artikkel.html', form=form, brukernavn=session['brukernavn'])


#Viser innloggingsskjema til bruker, og logger dem inn.
@app.route('/login', methods=['GET', 'POST'])
def login():
        form = forms.InnloggingSkjema(request.form)
        if request.method == 'POST' and form.validate():
                db = get_db()
                brukernavn = request.form['brukernavn']
                passord = request.form['passord']
                cur = db.execute('SELECT COUNT(id) FROM brukere WHERE navn = ? AND passord = ?', [brukernavn, passord])
                rad = cur.fetchone()[0]
                if int(rad) > 0:
                        session['brukernavn'] = brukernavn
                        session['passord'] = passord
                        return redirect(url_for('index'))
                flash('Feil brukernavn eller passord')
        return render_template('login.html', form=form)


#Legger inn en ny bruker i databasen
@app.route('/opprett_bruker', methods=['GET', 'POST'])
def opprett_bruker():
        form = forms.BrukerSkjema(request.form)
        if request.method == 'POST' and form.validate():
                db = get_db()
                brukernavn = request.form['brukernavn']
                passord = request.form['passord']
                cur = db.execute('SELECT COUNT(navn) FROM brukere WHERE navn = ?', [brukernavn])
                rad = cur.fetchone()[0]
                if int(rad) < 1:
                    db.execute(
                        'INSERT INTO brukere (navn, passord) values (?, ?)',
                        [brukernavn, passord])
                    db.commit()
                    session['passord'] = passord
                    session['brukernavn'] = brukernavn
                    flash('brukeren ble lagret i databasen')
                    return redirect(url_for('index'))
                flash('Brukeren eksisterer allerede')
        return render_template('opprett_bruker.html', form=form)

@app.route('/logg_ut')
def logg_ut():
    session.pop('passord')
    session.pop('brukernavn')
    return redirect(url_for('index'))

@app.route('/header')
def header():
    return render_template('header.html')

#Sørger for at riktig innloggingsinfo blir vist til bruker (logg inn/logg ut knapp osv.) i header
@app.route('/innlogging')
def innlogging():
        if 'brukernavn' not in session:
            brukernavn = ''
        else:
            brukernavn = session['brukernavn']
        return render_template('innlogging.html', brukernavn=brukernavn)

#Sletter en post fra databasen, blir kallt av JQuery (Ajax) på index-sida
@app.route('/delete/<post_id>', methods=['GET'])
def delete_entry(post_id):
    resultat = { 'status':0, 'message': 'Error'}
    if 'brukernavn' not in session:
        resultat = {'status':0, 'message': 'Ikke innlogget'}
    else:
        try:
            db = get_db()
            db.execute('DELETE FROM nyheter WHERE id = ?', [post_id])
            db.commit()
            resultat = {'status':1, 'message': 'Post Slettet'}
        except Exception as e:
            resultat = { 'status':0, 'message': repr(e) }

    return jsonify(resultat)

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
