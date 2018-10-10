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
        SELECT * FROM nyheter
    ''')

    rows = cur.fetchall()
    for row in rows:
        print(row)

print('Data has been retrieved successfully')
conn.close()
