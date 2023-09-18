import mysql.connector

yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '1234',
    autocommit = True
)

def LentokenttaLukumaaratTyypeittain(koodi):
    sql = "SELECT country.name AS 'maa', TYPE AS 'tyyppi', COUNT(airport.name) AS 'lukumäärä'"
    sql += "FROM airport, country "
    sql += "WHERE airport.iso_country = country.iso_country "
    sql += "AND country.iso_country = '" + koodi + "'"
    sql += "GROUP BY TYPE;"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount >0:
        for rivi in tulos:
            print(f"MAA: {rivi[0]}, TYYPPI: {rivi[1]}, LUKUMÄÄRÄ: {rivi[2]}")

maakoodi = input("Anna lentokentän maakoodi: ")
LentokenttaLukumaaratTyypeittain(maakoodi)