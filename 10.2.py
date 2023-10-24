class Hissi:
    def __init__(self, numero):
        self.numero = numero

    viimeisin = [[1], [1], [1]]

    def siirry_kerrokseen(self, kerros):

        if kerros > int(self.viimeisin[self.numero-1][0]):
            while kerros >= int(self.viimeisin[self.numero-1][0]):
                print(f"Olet kerroksessa {int(self.viimeisin[self.numero-1][0])}")
                self.kerros_ylos();
        elif kerros < int(self.viimeisin[self.numero-1][0]):
            while kerros < int(self.viimeisin[self.numero-1][0]):
                self.kerros_alas();
                print(f"Olet kerroksessa {int(self.viimeisin[self.numero-1][0])}")

    def kerros_ylos(self):
        self.luku = int(self.viimeisin[self.numero-1][0])
        self.luku += 1
        self.viimeisin[self.numero-1][0] = self.luku

    def kerros_alas(self):
        self.luku = int(self.viimeisin[self.numero-1][0])
        self.luku -= 1
        self.viimeisin[self.numero-1][0] = self.luku

class Talo:
    def __init__(self, alin, ylin, lukumaara):
        self.alin = alin
        self.ylin = ylin
        self.lukumaara = lukumaara

        self.hissit = []

        luku = 1
        for i in range(lukumaara):
            h = Hissi(luku)
            self.hissit.append(h)
            luku += 1

    def aja_hissia(self, numero, kohdekerros):
        print(f"\nAjat hissiä {numero}")
        self.hissit[numero-1].siirry_kerrokseen(kohdekerros)


talo = Talo(1, 7 , 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(2, 4)
talo.aja_hissia(3, 3)