class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin


    def siirry_kerrokseen(self, uusikerros):

        while self.kerros != uusikerros:
            print(f"Olet kerroksessa {self.kerros}")

            if self.kerros < uusikerros:
                self.kerros_ylos();
            elif self.kerros > uusikerros:
                self.kerros_alas();

        print(f"Olet kerroksessa {self.kerros}")
    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1

#PÄÄOHJELMA
class Talo:
    def __init__(self, alin, ylin, lukumaara):
        self.alin = alin
        self.ylin = ylin
        self.lukumaara = lukumaara
        self.hissit = [Hissi(alin, ylin) for i in range(lukumaara)]

    def aja_hissia(self, numero, kohdekerros):
        print(f"\nAjat hissiä {numero}")
        self.hissit[numero-1].siirry_kerrokseen(kohdekerros)


talo = Talo(1, 7 , 3)

talo.aja_hissia(2, 7)
talo.aja_hissia(2, 1)
talo.aja_hissia(1, 5)
talo.aja_hissia(1, 3)

