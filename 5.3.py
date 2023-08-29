luku = int(input("Anna luku: "))

flag = False

if luku == 1:
    print(f"{luku} ei ole alkuluku.")
elif luku > 1:
    for i in range(2,luku):
        if (luku % i) == 0:
            flag = True
            break

    if flag == True:
        print(f"{luku} ei ole alkuluku.")
    else:
        print(f"{luku} on alkuluku.")