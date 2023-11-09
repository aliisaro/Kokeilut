import random
class Auto:
    def __init__(self, tunnus, huippunopeus, nopeus=0, matka=0):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self):
        nopeus = random.randint(-10, 15)
        self.nopeus += nopeus

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
    def kulje(self):
        self.matka += self.nopeus

class Kilpailu:
    def __init__(self, nimi, kilometrimäärä, autolista):
        self.nimi = nimi
        self.kilometrimäärä = kilometrimäärä
        self.autolista = autolista


    def tunti_kuluu(self):

    def tulosta_tilanne(self):

    def kilpailu_ohi(self):


    autot = []
    for i in range(10):
        auto = Auto(f"ABC-{i + 1}", random.randint(100, 200))
        autot.append(auto)

