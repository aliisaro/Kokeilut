pituus = float(input("Anna kuhan pituus senttimetreinä: "))

pyyntimitta = 37

if pituus < pyyntimitta:
    alimitta = pyyntimitta - pituus
    print(f"Laske kuha takaisin järveen. Kuhan on {alimitta} senttimetriä alimittainen.")