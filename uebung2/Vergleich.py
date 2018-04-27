#! python3
import sys 
zahl1 = int(sys.argv[1])
zahl2 = int(sys.argv[2])
zahl3 = int(sys.argv[3])

if (zahl1 == zahl2) and (zahl2 == zahl3):
    print("Gleich")
elif (zahl1 < zahl2) and (zahl2 < zahl3):
    print("Aufsteigend Sortiert")
elif (zahl1 > zahl2) and (zahl2 > zahl3):
    print("Absteigend Sortiert")
else:
    print("Unsortiert")