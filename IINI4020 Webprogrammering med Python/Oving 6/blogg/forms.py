"""
	Øving 6
	19.10.2018
	Anders Kvanvig

    Python 3
"""
from wtforms import Form, StringField, PasswordField, TextAreaField, validators

class ArtikkelSkjema(Form):
    tittel = StringField('tittel', [validators.Length(min=4, max=50)])
    innhold = TextAreaField('innhold', [validators.Length(min=5)])

class InnloggingSkjema(Form):
	brukernavn = StringField('brukernavn', [validators.Length(min=4, max=25)])
	passord = PasswordField('passord', [validators.Length(min=4, max=35)])

class BrukerSkjema(Form):
	brukernavn = StringField('brukernavn', [validators.length(min=4, max=25)])
	passord = PasswordField('passord', [validators.length(min=4, max=35), validators.EqualTo('gjenta', message='Passord må være like')])
	gjenta = PasswordField('gjenta passord')
