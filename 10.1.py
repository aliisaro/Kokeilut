class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin

    viimeisin = [1]

    def siirry_kerrokseen(self, kerros):

        if kerros > int(self.viimeisin[-1]):
            while kerros >= int(self.viimeisin[-1]):
                print(f"Olet kerroksessa {int(self.viimeisin[-1])}")
                self.kerros_ylos(1);
        elif kerros < int(self.viimeisin[-1]):
            while kerros < int(self.viimeisin[-1]):
                self.kerros_alas(1);
                print(f"Olet kerroksessa {int(self.viimeisin[-1])}")

    def kerros_ylos(self, ylos):
        self.luku = int(self.viimeisin[-1])
        self.luku += ylos
        self.viimeisin.append(self.luku)

    def kerros_alas(self, alas):
        self.luku = int(self.viimeisin[-1])
        self.luku -= alas
        self.viimeisin.append(self.luku)

#PÄÄOHJELMA
h = Hissi(1, 7)

h.siirry_kerrokseen(5)
print("\n")
h.siirry_kerrokseen(1)