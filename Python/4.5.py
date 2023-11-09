tunnus = "python"
salasana = "rules"
yritykset = 0

while True:
    syote1 = input("Tunnus: ")
    syote2 = input("Salasana: ")

    if syote1 == tunnus and syote2 == salasana:
        print("Tervetuloa.")
        break
    else:
        print("Pääsy evätty.")
        yritykset += 1

    if yritykset == 5:
        break
