"""
	Øving 5
	29.09.2018
	Anders Kvanvig

    Python 3
"""

import sqlite3
conn = sqlite3.connect('blogg.db')
print('Opened database successfully')
#Oppretter tabellen nyheter med kolonner
conn.execute('''
    CREATE TABLE nyheter
    (id integer primary key autoincrement,
    tittel text not null,
    nyhet text not null,
    forfatter text not null);
    ''')
print('Created table nyheter successfully')
conn.close()
