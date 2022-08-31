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

    nama = "angge"
    umur = 22
    query = f"insert into kelas(nama, umur) values('{nama}', {umur})"

    curs.execute(query)
    conn.commit()
    print("data masuk")
except Exception as e:
    print (e)