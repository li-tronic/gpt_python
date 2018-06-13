import sys
zahl1 = int(sys.argv[1])
zahl2 = int(sys.argv[2])

print("", end="\t")
for elem  in range(zahl1,zahl2+1):
    print("{}".format(elem), end="\t")
print("\n")

for elem in range(zahl1,zahl2+1):
    print("{}".format(elem),end="\t")
    for prod in range(zahl1, zahl2+1):
        print("{}".format(elem*prod), end="\t")
    print("\t")