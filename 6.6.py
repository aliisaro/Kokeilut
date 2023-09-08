yksikkohinnat = []
def pizza(halkaisija, hinta):

    area = 3.14159 * pow((halkaisija / 2), 2)

    if hinta == hinta1 and halkaisija == halkaisija1:
        yksikkohinta1 = hinta / area
        yksikkohinnat.append(yksikkohinta1)
    else:
        yksikkohinta2 = hinta / area
        yksikkohinnat.append(yksikkohinta2)

        print(f"\nEkan pizzan yksikkohinta on {yksikkohinnat[0]:.3f} e/cm2.")
        print(f"Tokan pizzan yksikkohinta on {yksikkohinnat[1]:.3f} e/cm2.")

        if yksikkohinnat.index(min(yksikkohinnat)) == 0:
            print(f"Eka pizza antaa paremman vastineen rahalle.")
        elif yksikkohinnat.index(min(yksikkohinnat)) == 1:
            print(f"Toka pizza antaa paremman vastineen rahalle.")

hinta1 = float(input("Ekan pizzan hinta (e): "))
halkaisija1 = float(input("Ekan pizzan halkaisija (cm): "))
pizza(halkaisija1, hinta1)

hinta2 = float(input("Tokan pizzan hinta (e): "))
halkaisija2 = float(input("Tokan pizzan halkaisija (cm): "))
pizza(halkaisija2, hinta2)

