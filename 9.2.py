class Auto:
    def __init__(self, tunnus, huippunopeus, nopeus=0, matka=0):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if muutos > 0:
            if self.nopeus > self.huippunopeus:
                print(f"Auton nopeus: {self.huippunopeus} km/h")
            else:
                print(f"Auton nopeus: {self.nopeus} km/h")
        elif muutos < 0:
            if self.nopeus < 0:
                print(f"Auton nopeus jarrutuksen jälkeen: 0 km/h")
            else:
                print(f"Auton nopeus jarrutuksen jälkeen: {auto.nopeus} km/h")
        return

auto = Auto("ABC-123", 142)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
auto.kiihdyta(-200)