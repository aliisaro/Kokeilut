while True:
    tuumat = float(input("Anna tuumat: "))

    if tuumat >= 0:
        sentit = tuumat * 2.54
        print(f"{tuumat} tuumaa senttimetreinä on {sentit}")
    else:
        break