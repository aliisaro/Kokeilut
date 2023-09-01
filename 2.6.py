import random
x = 0
code1 = ""

while (x < 3) :
    number = str(random.randint(0,9))
    code1 = code1 + number
    x +=1

print (code1)

x = 0
code2 = ""

while (x < 4) :
    number = str(random.randint(1,6))
    code2 = code2 + number
    x +=1

print(code2)