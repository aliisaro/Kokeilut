luvut = []

while True:
    luku = input("Anna luku: ")

    if luku == "":
        break
    else:
        luvut.append(int(luku))

print(f"Pienin antamasi luku on {min(luvut)} ja suurin luku on {max(luvut)}.")