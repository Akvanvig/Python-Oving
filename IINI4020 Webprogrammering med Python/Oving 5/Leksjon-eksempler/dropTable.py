"""
	Øving 5
	29.09.2018
	Anders Kvanvig

    Python 3
"""

import sqlite3
conn = sqlite3.connect('blogg.db')
print('Opened database successfully')
#Sletter tabellen fra databasen
conn.execute('''
    DROP TABLE nyheter
''')
print('Dropped table nyheter successfully')
conn.close()
