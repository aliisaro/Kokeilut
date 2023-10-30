class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}")
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumäärä):
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjailija: {self.kirjailija} \nSivumäärä: {self.sivumäärä}")
class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.päätoimittaja}")

#PÄÄOHJELMA
julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for i in julkaisut:
    i.tulosta_tiedot()
    print("\n")