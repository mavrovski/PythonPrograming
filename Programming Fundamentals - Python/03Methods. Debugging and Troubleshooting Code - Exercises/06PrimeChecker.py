import math

def is_prime(number):
    prime = True
    if  number<2 :
        prime = bool(0)
    else:
        for i in range(2,int(math.sqrt(number))+1):
            if number % i == 0:
                prime = False
                break
    if prime:
        return prime
    else:
        return prime


number = int(input())
print(is_prime(number))