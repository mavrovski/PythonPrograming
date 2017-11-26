array_one = input().split(' ')
array_two = input().split(' ')

array_one_length = len(array_one)
array_two_length = len(array_two)

short_array = min(array_one_length,array_two_length)

for i in range (0,short_array):
    if array_one[i] != array_two[i]:
        if array_one[i]<array_two[i]:
            print(''.join(array_one))
            print(''.join(array_two))
            break
        else:
            print(''.join(array_two))
            print(''.join(array_one))
            break


    if array_one_length<array_two_length:
        print(''.join(array_one))
        print(''.join(array_two))
        break
    else:
        print(''.join(array_two))
        print(''.join(array_one))
        break