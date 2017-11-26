array_one = input().split(' ')
array_two = input().split(' ')

array_one_count = 0
array_two_count = 0
smaller_array  = min(len(array_one),len(array_two))

for i in range (0,smaller_array):
    if array_one[i] == array_two[i]:
        array_one_count += 1
    if array_one[len(array_one)-1-i] == array_two[len(array_two)-1-i]:
        array_two_count+=1
print(max(array_one_count,array_two_count))