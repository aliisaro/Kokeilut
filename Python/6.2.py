import random
def noppa(max):
    heitto = 0

    while heitto != max:
        heitto = random.randint(1, max)
        print(heitto)

max = int(input("Anna nopan maksimisilmäluku: "))
noppa(max)