luvut = []

luku = input("Anna luku: ")

while luku != "":
    luvut.append(int(luku))
    luku = input("Anna luku: ")

    if luku == "":
        luvut.sort(reverse=True)

for i in luvut[:5]:
    print(i)


