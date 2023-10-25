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

autot = []

for i in range(10):
    auto = Auto(f"ABC-{i+1}", random.randint(100, 200))
    autot.append(auto)

while all(auto.matka < 10000 for auto in autot):

    for auto in autot:
        auto.kiihdyta()
        auto.kulje()
        print(auto.tunnus, auto.matka)

print("\nTulokset: ")

for auto in autot:
    print(f"Rekkari: {auto.tunnus}, huippunopeus: {auto.huippunopeus}, nopeus lopusssa: {auto.nopeus}, kuljettu matka: {auto.matka}")


