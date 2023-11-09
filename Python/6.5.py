def listat(kokonaisluvut):

    karsittu = []
    for num in kokonaisluvut:
        if num % 2 == 0:
            karsittu.append(num)

    return karsittu

karsitaan = [1,2,3,4,5,6,7,8,9,10]
listat(karsitaan)
print(karsitaan)
print(listat(karsitaan))

