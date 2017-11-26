number = int(input())
primes=[bool]*int(number+1)

for i in range (0,len(primes)):
    primes[i]=True

primes[0]=primes[1]=False

for i in range (0,number+1):
    if primes[i]!=True:
        continue
    print("{0} ".format(i),end='')
    for p in range (2*i,number+1,i):
        primes[p]=False
print()