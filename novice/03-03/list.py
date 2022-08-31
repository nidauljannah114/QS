# try:
# from . import connection
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="siswa",
    user="postgres",
    password="nida")

# except Exception as e:
#     print(e)

curs = conn.cursor()
query = f"select * from kelas"
curs.execute(query)
data = curs.fetchall()
if not data:
    print("gak ada")

for d in data:
    print("nama:", d[0], "umur:", d[1])