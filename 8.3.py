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

def LentokenttienEtaisyys(ICAO1, ICAO2):
    sql = "SELECT latitude_deg, longitude_deg FROM airport "
    sql += "WHERE ident = '" + ICAO1 + "'"
    sql += "OR ident = '" + ICAO2 + "'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    #print(tulos[0], tulos[1])

    print(f"Lentokenttien välinen matka kilometreinä: {distance.distance(tulos[0], tulos[1]).km:.3f}")
    return

ICAO1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
ICAO2 = input("Anna toisen lentokentän ICAO-koodi: ")
LentokenttienEtaisyys(ICAO1, ICAO2)

