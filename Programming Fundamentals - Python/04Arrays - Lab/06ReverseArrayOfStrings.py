array_of_strings = input().split(' ')
# array_of_strings.reverse()  //or
for i in array_of_strings[::-1]:
    print("{0} ".format(i),end='')
# print(' '.join(input().split(' ')[::-1])) //on one line