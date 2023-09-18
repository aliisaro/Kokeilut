import mysql.connector

yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '1234',
    autocommit = True
)

def LentokenttaNimi(koodi):
    sql = "SELECT name, municipality FROM airport WHERE ident = '" + koodi + "'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount >0:
        for rivi in tulos:
            print(f"Lentokentän nimi on '{rivi[0]}' ja sijaintikunta on '{rivi[1]}'.")

ICAO = input("Anna lentokentän ICAO-koodi: ")
LentokenttaNimi(ICAO)