leiviskamaara = float(input("Anna leiviskät: "))
naulamaara = float(input("Anna naulat: "))
luotimaara = float(input("Anna luodit: "))

luodit = luotimaara * 13.3
naulat = naulamaara * (32 * 13.3)
leiviskat = leiviskamaara * (20 * 32 * 13.3)

massa = luodit + naulat + leiviskat #grammoina

kg = int(massa//1000)
g = massa-1000*kg

print(f"Massa nykymittojen mukaan: {kg} kilogrammaa ja {g:.2f} grammaa.")
