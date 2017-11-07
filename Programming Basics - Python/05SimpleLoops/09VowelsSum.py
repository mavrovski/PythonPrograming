word = input()

sumOfChars = 0

for i in word:
    if i == 'a':
        sumOfChars+=1
    elif i == 'e':
        sumOfChars+=2
    elif i == 'i':
        sumOfChars+=3
    elif i == 'o':
        sumOfChars+=4
    elif i == 'u':
        sumOfChars+=5
print(sumOfChars)
