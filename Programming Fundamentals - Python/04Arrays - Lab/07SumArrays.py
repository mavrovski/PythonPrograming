array_one = list(map(int,input().split(' ')))
array_two = list(map(int,input().split(' ')))

len_one = int(len(array_one))
len_two = int(len(array_two))
max_length = max(len_one,len_two)

sum_of_elements = []

for i in range (0,max_length):
    sum_of_elements.append(array_one[i%len_one]+array_two[i%len_two])

for number in sum_of_elements:
    print("{0} ".format(number),end='')
