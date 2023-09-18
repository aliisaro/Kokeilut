nimet = set()

nimi = "pepe"
while nimi != "":
    nimi = input("Anna nimi: ")

    if nimi in nimet:
        print("Aiemmin syötetty nimi.\n")
    else:
        print("Uusi nimi.\n")
        nimet.add(nimi)

