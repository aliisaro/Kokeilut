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

class Talo:
    def __init__(self, alin, ylin, lukumaara):
        self.alin = alin
        self.ylin = ylin
        self.lukumaara = lukumaara
        self.hissit = [Hissi(alin, ylin) for i in range(lukumaara)]

    def aja_hissia(self, numero, kohdekerros):
        print(f"\nAjat hissiä {numero}")
        self.hissit[numero-1].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        luku = 1
        for hissi in self.hissit:
            print(f"Palohälytys!!! Hissi on {luku}  kerroksesssa {hissi.kerros}.")
            hissi.kerros = self.hissit[0].alin
            print(f"Hissi on {luku} siirtyi kerrokseen {hissi.kerros}.\n")
            luku += 1

#PÄÄOHJELMA
talo = Talo(1, 7 , 3)
talo.aja_hissia(1, 7)
talo.aja_hissia(2, 3)
talo.aja_hissia(3, 2)
print("\n")
talo.palohälytys()
