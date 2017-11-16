import math

n = int(input())

for i in range(2,n+1):
    mathSqrt = int(math.sqrt(i))
    isPrime = True
    for j in range(2,mathSqrt+1):
        if i % j == 0:
            isPrime = False
    print("{0} -> {1}".format(i,isPrime))

    