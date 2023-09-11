nimet = set()

while True:
    nimi = input("Anna nimi: ")

    if nimi in nimet:
        print("Aiemmin syötetty nimi.\n")
    elif nimi == "":
        break
    else:
        print("Uusi nimi.\n")

    nimet.add(nimi)

