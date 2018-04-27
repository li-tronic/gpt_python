#! python3
zahl1 = int(input("Zahl 1: "))
zahl2 = int(input("Zahl 2: "))

if (zahl1 % zahl2 == 0) or (zahl2 % zahl1 == 0 ):
    print(True)
else:
    print(False)
