luvut = []
luku = input("Anna luku: ")

while luku!= "":
    luvut.append(int(luku))
    luku = input("Anna luku: ")

print(f"Pienin antamasi luku on {min(luvut)} ja suurin luku on {max(luvut)}.")