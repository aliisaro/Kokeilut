import random

x = random.randrange(1,11)

while True:
    arvaus = int(input("Arvaa luku: "))

    if arvaus > x:
        print("Liian suuri arvaus.")
    elif arvaus < x:
        print("Liian pieni arvaus.")
    else:
        print("Oikein!")
        break



