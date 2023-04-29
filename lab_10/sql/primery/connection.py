import psycopg2
from config import data

con = psycopg2.connect(**data)
cursor = con.cursor()

query = f"""


"""


cursor.close()
con.close()
