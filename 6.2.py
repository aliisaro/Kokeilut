import random

max = int(input("Anna nopan maksimisilmäluku: "))
def noppa(tahko):

    while True:
        luku = random.randrange(1,max+1)
        print(luku)
        if luku == tahko:
            break
noppa(max)