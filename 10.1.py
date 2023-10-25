class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin


    def siirry_kerrokseen(self, uusikerros):

        while self.kerros != uusikerros:

            #if uusikerros > self.ylin:
                #print(f"Olet kerroksessa {self.ylin}")
            #elif uusikerros < self.alin:
                #print(f"Olet kerroksessa {self.alin}")
            #else:

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
h = Hissi(1, 7)

h.siirry_kerrokseen(7)
print("\n")
h.siirry_kerrokseen(1)