class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin

    viimeisin = [1]

    def siirry_kerrokseen(self, kerros):
        self.kerros = kerros

        if self.kerros > int(self.viimeisin[-1]):
            while self.kerros >= int(self.viimeisin[-1]):
                print(f"Olet kerroksessa {int(self.viimeisin[-1])}")
                self.kerros_ylos(1);
        elif self.kerros < int(self.viimeisin[-1]):
            while self.kerros < int(self.viimeisin[-1]):
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

class Talo:
    def __init__(self, alin, ylin, lukumaara):
        self.alin = alin
        self.ylin = ylin
        self.hissilista = [lukumaara]

    def aja_hissia(self, numero, kohdekerros):



h = Hissi(1, 7)
h.siirry_kerrokseen(5)
print("\n")
h.siirry_kerrokseen(1)

talo = Talo(1, 7 , 3)

talo.aja_hissia(2, 7)


