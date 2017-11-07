import math


n=int(input())
prime = bool(1)
if  n<2 :
    prime = bool(0)
else:
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            prime = bool(0)
            break

if prime:
    print("Prime")
else:
    print("Not Prime")