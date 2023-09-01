sukupuoli = input("Mikä on biologinen sukupuolesi (nainen/mies): ")
arvo = int(input("Mikä on hemoglobiiniarvosi?: "))

if sukupuoli == "Nainen" or "nainen":
    if arvo > 175:
        print("Hemoglobiini arvosi on korkea.")
    elif arvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

    print("Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.")

elif sukupuoli == "Mies" or "mies":
    if arvo > 195:
        print("Hemoglobiini arvosi on korkea.")
    elif arvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

    print("Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.")