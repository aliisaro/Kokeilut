class Auto:
    def __init__(self, tunnus, huippunopeus, nopeus=0, matka=2000):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, muutos):
        if muutos > 0:
            self.nopeus += muutos
            if self.nopeus > self.huippunopeus:
                print(f"Auton nopeus: {self.huippunopeus} km/h")
            else:
                print(f"Auton nopeus: {self.nopeus} km/h")
        elif muutos < 0:
            self.nopeus += muutos
            if self.nopeus < 0:
                print(f"Auton nopeus jarrutuksen jälkeen: 0 km/h")
            else:
                print(f"Auton nopeus jarrutuksen jälkeen: {auto.nopeus} km/h")
        return

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit
        print(f"Auton kulkema matka: {auto.matka} km")


auto = Auto("ABC-123", 142)

auto.kiihdyta(60)
auto.kulje(1.5)
