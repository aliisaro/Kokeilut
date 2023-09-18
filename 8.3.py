import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '1234',
    autocommit = True
)

def LentokenttienEtaisyys(koodi1, koodi2):
    sql1 = "SELECT latitude_deg, longitude_deg FROM airport "
    sql1 += "WHERE ident = '" + koodi1 + "'"


    kursori = yhteys.cursor()
    kursori.execute(sql1)
    tulos = kursori.fetchall()

    if kursori.rowcount >0:
        for rivi in tulos:
            paikka1 = (rivi[0], rivi[1])

    sql2 = "SELECT latitude_deg, longitude_deg FROM airport "
    sql2 += "WHERE ident = '" + koodi2 + "'"

    kursori = yhteys.cursor()
    kursori.execute(sql2)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            paikka2 = (rivi[0], rivi[1])

    print(f"Lentokenttien välinen matka kilometreinä: {distance.distance(paikka1, paikka2).kilometers:0.3f}")

ICAO1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
ICAO2 = input("Anna toisen lentokentän ICAO-koodi: ")
LentokenttienEtaisyys(ICAO1, ICAO2)


#YKSI SQL-LAUSE
#sql = "SELECT latitude_deg, longitude_deg FROM airport "
#sql += "WHERE ident IN ('" + koodi1 + "', '" + koodi2 + "')"