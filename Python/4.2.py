tuumat = 1

while tuumat > 0:
    tuumat = float(input("Anna tuumamäärä: "))
    sentteina = tuumat * 2.54
    if tuumat > 0:
        print(f"Tuumat sentteinä: {sentteina}")
