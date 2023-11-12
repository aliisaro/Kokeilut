class Auto:
    def __init__(self, tunnus, huippunopeus, nopeus=0, matka=0):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def tulosta_tiedot(self):
        print(f"{self.tunnus}, {self.huippunopeus}, {self.nopeus}, {self.matka}")

class Sähköauto(Auto):
    def __init__(self, tunnus, huippunopeus, nopeus, matka, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(tunnus, huippunopeus, nopeus, matka)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.akkukapasiteetti}")


#PÄÄOHJLEMA
auto = Sähköauto("ABC-15", 180, 80, 0, 52.5)
auto.tulosta_tiedot()
