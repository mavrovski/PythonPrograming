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
        return True
    else:
        return False

def find_primes_in_range(start_num,end_num):
    result = []
    for i in range (start_num,end_num+1):
        if is_prime(i):
            result.append(i)
    return result

start_num = int(input())
end_num = int(input())
primes_in_range = find_primes_in_range(start_num,end_num)
print(', '.join(map(str,primes_in_range)))
