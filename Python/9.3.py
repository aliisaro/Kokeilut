class Auto:
    def __init__(self, tunnus, huippunopeus, nopeus=0, matka=0):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, muutos):

        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            print(f"Auton nopeus: {self.huippunopeus} km/h")
        elif self.nopeus < 0:
            print(f"Auton nopeus: 0 km/h")
        else:
            print(f"Auton nopeus: {self.nopeus} km/h")

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit
        print(f"Auton kulkema matka: {auto.matka} km")


auto = Auto("ABC-123", 142, 0, 2000)

auto.kiihdyta(60)
auto.kulje(1.5)
