from flask import Flask, render_template
import psycopg2
import psycopg2.extras

app = Flask(__name__)

app.secret_key = "caircocoders-ednalan"
# @app.route("/")
# def index():
    # return render_template("index.html")
conn = psycopg2.connect(
    host="localhost",
    database="project",
    user="postgres",
    password="nida"
    )

@app.route("/")
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM umkjogja ORDER BY id")
    umkjogja = cur.fetchall()
    return render_template('index.html', umkjogja = umkjogja)
    

if __name__== "__main__":
    app.run(host="0.0.0.0", port=8080)      