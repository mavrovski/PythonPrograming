def zero_counter(factorial):
    zero_counter = 0
    has_zero = True
    while has_zero == True:
        digit = int(factorial%10)
        factorial = int(factorial//10)
        if digit==0:
            zero_counter+=1
        else:
            has_zero = False

    print(zero_counter)


n = int(input())
factorial = int(1)
for i in range (1,n+1):
    factorial *= i
zero_counter(factorial)
