class Auto:
    def __init__(self, tunnus, huippunopeus, nopeus=0, matka=0):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            print(f" Nopeus: {self.huippunopeus} km/h")
        elif self.nopeus < 0:
            print(f" Nopeus: 0 km/h")
        else:
            print(f" Nopeus: {self.nopeus} km/h")

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit
        print(f" Kuljettu matka {tunnit} tunnissa: {auto.matka} km")

class Sähköauto(Auto):
    def __init__(self, tunnus, huippunopeus, nopeus, matka, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(tunnus, huippunopeus, nopeus, matka)

class Polttomoottoriauto(Auto):
    def __init__(self, tunnus, huippunopeus, nopeus, matka, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(tunnus, huippunopeus, nopeus, matka)



#PÄÄOHJLEMA
auto = Sähköauto("ABC-15", 180, 0, 0, 52.5)
print(f" Rekisteritunnus: {auto.tunnus}, huippunopeus: {auto.huippunopeus} km/h ja akkukapasiteetti {auto.akkukapasiteetti} kWh")
auto.kiihdyta(80)
auto.kulje(3)
print(f" Matkamittarilukema: {auto.matka}")

print("\n")

auto = Polttomoottoriauto("ACD-123", 16, 0, 0, 32.3)
print(f" Rekisteritunnus: {auto.tunnus}, huippunopeus: {auto.huippunopeus} km/h ja bensatankki: {auto.bensatankki} l")
auto.kiihdyta(60)
auto.kulje(3)
print(f" Matkamittarilukema: {auto.matka}")

