import random

luku = random.randint(1, 10)
arvaus = -1

while arvaus != luku:
    arvaus = int(input("Arvaa luku: "))
    if arvaus < luku:
        print("Liian pieni arvaus.")
    elif arvaus > luku:
        print("Liian suuri arvaus.")
    else:
        print("Oikein!")