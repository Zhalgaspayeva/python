import psycopg2
from config import data

connect = psycopg2.connect(**data)
cursor = connect.cursor()
query = '''



'''