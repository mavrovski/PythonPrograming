n = int(input())
f0= 1
f1 = 1
for i in range(0,n-1):
    fnext = f0+f1
    f0 = f1
    f1 = fnext
print(f1)
