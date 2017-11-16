def is_palindrome(number):
    number_to_string = str(number)
    reverse_number = ""
    for i in range(len(number_to_string) - 1, -1, -1):
        reverse_number += number_to_string[i]
    if reverse_number == number_to_string:
        return True
    else:
        return False

def sum_of_digits(number):
    if number % 7 == 0:
        return True
    else:
        return False

def contains_even_digit(number):
    result = 0
    has_even = False
    divisible = False
    while number>0:
        digit = int(number % 10)
        number /= 10
        if digit % 2 == 0:
            has_even = True
        else:
            has_even = False
        result+=int(digit)

    if result % 7 == 0:
        divisible = True
    if has_even and divisible:
        return True
    else:
        return False



number = int(input())

for i in range (0,number):
    if is_palindrome(i) == True and contains_even_digit(i):
        print(i)

