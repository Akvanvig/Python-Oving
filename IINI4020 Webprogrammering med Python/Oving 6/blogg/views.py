"""
	Øving 6
	19.10.2018
	Anders Kvanvig

    Python 3
"""
from flask import Flask, request, g, redirect, url_for, abort, render_template, flash, jsonify
#pner index-sida og viser nyheter/innlegg
@app.route('/')
def index():
    db = get_db()
    cur = db.execute('SELECT * FROM nyheter ORDER BY id DESC')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)

#Åpner sida for å opprette en nyhet/et innlegg
@app.route('/opprett_artikkel')
def opprett_artikkel():
	form = forms.ArtikkelSkjema()
	render_template('opprett_artikkel.html', form=form)

#Legger inn nyhet/innlegg i databasen
@app.route('/add_nyhet', methods=['POST'])
def add_nyhet():
    db = get_db()
    db.execute(
        'INSERT INTO nyheter (tittel, nyhet, forfatter) values (?, ?, ?)',
        [request.form['tittel'], request.form['nyhet'], request.form['forfatter']]
    )
    db.commit()
    flash('innlegget ble sendt og lagret i databasen')
    return redirect(url_for('index'))

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
	form = forms.InnloggingSkjema()
	#if form.validate_on_submit():
	#	pass
	return render_template('login.html', form=form)
