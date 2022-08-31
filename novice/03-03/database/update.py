try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="siswa",
        user="postgres",
        password="nida")

# except Exception as e:
#     print(e)

    curs = conn.cursor()

    namaLama = "angge"
    
    namaBaru = "anggang"
    umurBaru = 24
    query = f"update kelas set nama='{namaBaru}', umur={umurBaru} where nama='{namaLama}'"

    curs.execute(query)
    conn.commit()
    print("data masuk")
except Exception as e:
    print (e)