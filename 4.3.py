luvut = []

while True:

    try:
        luku = float(input("Anna luku: "))
        luvut.append(luku)

    except ValueError:
        break

print(f"Pienin antamasi luku on {min(luvut)} ja suurin luku on {max(luvut)}.")