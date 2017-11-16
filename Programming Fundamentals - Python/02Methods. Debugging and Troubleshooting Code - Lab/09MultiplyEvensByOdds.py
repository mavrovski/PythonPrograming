def get_sum_of_evens(num):
    sum = 0
    while num>0:
        lastDigit = int(num%10)
        if lastDigit % 2 == 0:
            sum+=int(lastDigit)
        num/=10
    return sum

def get_sum_of_odds(num):
    sum = 0
    while num > 0:
        lastDigit = int(num % 10)
        if lastDigit % 2 != 0:
            sum += int(lastDigit)
        num /= 10
    return sum

def get_multiple_evens_and_odds(num):
    sumOfEvens = get_sum_of_evens(num)
    sumOfOdds = get_sum_of_odds(num)
    return  sumOfEvens*sumOfOdds


num = int(input())
print(get_multiple_evens_and_odds(abs(num)))