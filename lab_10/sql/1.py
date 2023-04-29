import psycopg2
from config import data

con = psycopg2.connect(**data)
cursor = con.cursor()

query = '''

SELECT * from phone_book
'''

cursor.execute(query)

#cursor.execute(query1)

a = cursor.fetchall()


con.close