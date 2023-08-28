import random

arpakuutiot = int(input("Anna arpakuutioiden määrä: "))
silmaluvut = []

for luku in range(arpakuutiot):
    silmaluku = random.randrange(1,6)
    silmaluvut.append(silmaluku)

print(sum(silmaluvut))


