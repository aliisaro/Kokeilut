import random

luku = 0
n = 0 #ympyrän sisälle jäävät pisteet

#kysytään pisteiden lukumäärää
N = int(input("Anna pisteiden määrä: "))

while luku < N:

    #arvotaan piste nelion sisältä
    x = random.randrange(-1,1)
    y = random.randrange(-1,1)

    #lasketaan jos piste on nelion sisällä olevan ympyrän sisällä
    if x^2+y^2<1:
        n += 1

    luku += 1

#lasketaan ja tulostetaan piin likiarvo
approx = sum([4/i - 4/(i+2) for i in range(1, 2*n+1, 4)])
print(approx)

#print(pii≈4n/N)