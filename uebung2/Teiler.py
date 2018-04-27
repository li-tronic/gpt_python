#! python3
import sys
nenner = int(sys.argv[1])

for teiler in range(1,nenner+1):
    mod = nenner%teiler
    if mod == 0:
        print(teiler)