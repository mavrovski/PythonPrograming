def sum_of_digits(n):
    sum_of_digit = 0
    while n > 0:
        digit = n % 10
        sum_of_digit += int(digit)
        n /= 10;
    if sum_of_digit % 7 == 0:
        return True
    return False

def is_contains_even_digit(number):

    while number > 0:
        currentDigit = number % 10
        if currentDigit % 2 == 0:
            return True
        number = int(number / 10)
    return False




def is_palindrome(number):
    number_to_string = str(number)
    reverse_number = ""
    for i in range(len(number_to_string) - 1, -1, -1):
        reverse_number += number_to_string[i]
    if reverse_number == number_to_string:
        return True
    else:
        return False


n = int(input())
for number in range (0,n):
    if sum_of_digits(number) and is_contains_even_digit(number) and is_palindrome(number):
        print(number)