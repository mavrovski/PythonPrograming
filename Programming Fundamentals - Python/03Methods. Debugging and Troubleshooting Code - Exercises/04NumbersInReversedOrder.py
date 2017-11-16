def reverse_number(number):
    reverse = ""
    for i in range(len(number)-1,-1,-1):
        reverse += number[i]
    return reverse

number = input()
print(reverse_number(number))