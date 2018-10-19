"""
	Øving 6
	16.10.2018
	Anders Kvanvig

    Python 3
"""
from wtforms import Form, StringField, PasswordField, validators

class ArtikkelSkjema(Form):
    tittel = StringField('tittel', [validators.DataRequired()])
    innhold = StringField('innhold', [validators.DataRequired()])
    forfatter = StringField('forfatter', [validators.DataRequired()])

class InnloggingSkjema(Form):
	brukernavn = StringField('brukernavn', [validators.Length(min=4, max=25)])
	passord = PasswordField('passord', [validators.Length(min=4, max=25)])
