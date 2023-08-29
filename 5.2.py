luvut = []

while True:
    luku = input("Anna luku: ")

    if luku == "":
        luvut.sort(reverse=True)
        break
    else:
        luvut.append(int(luku))

for i in luvut[:5]:
    print(i)


