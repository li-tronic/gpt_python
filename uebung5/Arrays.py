import sys
a = []
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
a.append(float(input()))
print((a[0]+a[1]+a[2]+a[3])/4)
a.sort(reverse=True)
b =[]
b.append(a[0])
b.append(a[1])
print(b)