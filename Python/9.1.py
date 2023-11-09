class Auto:
    def __init__(self, tunnus, huippunopeus, nopeus=0, matka=0):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

auto = Auto("ABC-123", 142)

print(f" Rekisteritunnus: {auto.tunnus}\n Huippunopeus: {auto.huippunopeus} km/h \n Nopeus = {auto.nopeus} km/h \n Kuljettu matka: {auto.matka} km")
