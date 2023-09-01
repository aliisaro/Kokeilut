leiviskamaara = int(input("Anna leiviskät: "))
naulamaara = int(input("Anna naulat: "))
luotimaara = float(input("Anna luodit: "))

luodit = luotimaara * 13.3
naulat = naulamaara * (32 * 13.3)
leiviskat = leiviskamaara * (20 * 32 * 13.3)

massa = luodit + naulat + leiviskat #grammoina

print(f"Massa nykymittojen mukaan: {massa} grammaa")
