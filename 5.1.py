import random

arpakuutiot = int(input("Anna arpakuutioiden määrä: "))
silmaluvut = []

for luku in range(arpakuutiot):
    silmaluku = random.randint(1,6)
    print(silmaluku)
    silmaluvut.append(silmaluku)

print(sum(silmaluvut))


