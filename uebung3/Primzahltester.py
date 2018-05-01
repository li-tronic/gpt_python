#! python3
import sys

zahl = int(sys.argv[1])
for x in range(2,zahl):
    test = zahl % x
    if test == 0:
        print("False")
        break

else:
    print("True")