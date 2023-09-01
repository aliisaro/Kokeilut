sukupuoli = input("Mikä on biologinen sukupuolesi (nainen/mies): ").lower()
arvo = int(input("Mikä on hemoglobiiniarvosi?: "))

if sukupuoli == "nainen":
    if arvo > 175:
        print("Hemoglobiini arvosi on korkea.")
    elif arvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

    print("Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.")

elif sukupuoli == "mies":
    if arvo > 195:
        print("Hemoglobiini arvosi on korkea.")
    elif arvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

    print("Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.")