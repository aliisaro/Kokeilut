lentoasemat = {}
syote = "moi"

while syote != "lopeta":
    syote = input("Valitse 'uusi lentoasema', 'lentoaseman tiedot' tai 'lopeta':")

    if syote.lower() == "uusi lentoasema":
        ICAO = input("Lentoaseman ICAO-koodi: ")
        nimi = input("Lentoaseman nimi: ")
        lentoasemat['ICAO'] = nimi
    elif syote.lower() == "lentoaseman tiedot":
        ICAO = input("Lentoaseman ICAO-koodi: ")
        print(lentoasemat['ICAO'])

