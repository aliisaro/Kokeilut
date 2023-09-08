import math
def pizza(halkaisija, hinta):

    area = ((math.pi * halkaisija) / 100) / 100

    yksikkohinta = hinta / area

    return yksikkohinta

hinta1 = float(input("Ekan pizzan hinta (e): "))
halkaisija1 = float(input("Ekan pizzan halkaisija (cm): "))
pizza(halkaisija1, hinta1)
eka = pizza(halkaisija1, hinta1)

hinta2 = float(input("Tokan pizzan hinta (e): "))
halkaisija2 = float(input("Tokan pizzan halkaisija (cm): "))
pizza(halkaisija2, hinta2)
toka = pizza(halkaisija2, hinta2)


if eka < toka:
    print(f"Eka pizza antaa paremman vastineen rahalle.")
else:
    print(f"Toka pizza antaa paremman vastineen rahalle.")
