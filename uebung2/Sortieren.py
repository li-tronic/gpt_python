#! python3

namen = []
for i in range(1,4):
    namen.append(input("Name{0}: ".format(i)))

namen = sorted(namen)

for name in namen:
    print(name)