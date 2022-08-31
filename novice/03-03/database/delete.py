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

    nama = "anggi"
    query = f"delete from kelas where nama='{nama}'"

    curs.execute(query)
    conn.commit()
    print("data berhasil dihapus")
except Exception as e:
    print (e)