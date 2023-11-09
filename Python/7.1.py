talvi = ("12", "1", "2")
kevat = ("3", "4", "5")
kesa = ("6", "7", "8")
syksy = ("9", "10", "11")

luku = input("Anna kuukauden numero: ")

if luku in talvi:
    print("Talvi")
elif luku in kevat:
    print("Kevät")
elif luku in kesa:
    print("Kesä")
else:
    print("Syksy")