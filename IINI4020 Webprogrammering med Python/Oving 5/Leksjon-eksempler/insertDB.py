"""
	Øving 5
	29.09.2018
	Anders Kvanvig

    Python 3
"""
import sqlite3

conn = sqlite3.connect('blogg.db')
print('Opened database successfully')

with conn:
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO nyheter VALUES(1, 'Sportsnytt', 'Landslaget vant', 'Ola Normann')
        ''')
    cur.execute('''
        INSERT INTO nyheter (tittel, nyhet, forfatter) VALUES ('Utenriksnytt', 'WTO møtet avlyst', 'Alfred Nobel')
    ''')

print('Data was inserted successfully')
conn.close()
