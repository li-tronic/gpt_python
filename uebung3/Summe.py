#! python3

print("Dieses Programm berechnet die Summe der eingegebenen Zahlen. Eingabe 0 beendetdas Programm.")

eingabe = 1
summe = 0
while eingabe  != float(0):
    
     eingabe = float(input("Bitte geben Sie eine Kommazahl ein:"))
     summe += eingabe
print("Summe: {}".format(summe))