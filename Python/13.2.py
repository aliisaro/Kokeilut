from flask import Flask, request
import mysql.connector

yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '1234',
    autocommit = True
)

app = Flask(__name__)
@app.route('/kenttä')
def kenttä():
    args = request.args
    ICAO = str(args.get("ICAO"))

    sql = "SELECT name, municipality FROM airport WHERE ident = '" + ICAO + "'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            airport = rivi[0]
            city = rivi[1]

    vastaus = {
        "ICAO": ICAO,
        "Name": airport,
        "Municipality": city
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
