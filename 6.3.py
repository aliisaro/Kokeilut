def bensiini(maara):

    while True:
        litrat = 3.785 * maara

        if maara >= 0:
            print(f"Litroina: {litrat}")
        else:
            break

        maara = float(input("Anna gallonamäärä: "))

gallons = float(input("Anna gallonamäärä: "))
bensiini(gallons)