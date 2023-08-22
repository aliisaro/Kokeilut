leiviskamaara = int(input("Anna leiviskät: "))
naulamaara = int(input("Anna naulat: "))
luotimaara = float(input("Anna luodit: "))

luodit = luotimaara * 13.3
naulat = naulamaara * (32 * 13.3)
leiviskat = leiviskamaara * (20 * 32 * 13.3)

massa = luodit + naulat + leiviskat #grammoina

y = str(massa/1000).split('.')

a = y[0]
b = y[1]

c = float(b) / 100

print(massa)

print(f"Massa nykymittojen mukaan: {a} kilogrammaa ja {c} grammaa")
