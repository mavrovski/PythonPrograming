n = int(input())
k = int(input())
sequence=[n]
sequence[0]=1


def sum_numbers(numbers,start_index,end_index):
    sum = 0
    for i in range (start_index,end_index):
        sum+=numbers[i]
    return sum


for i in range(1,n):
    begin = 0
    if i>=k:
        begin = i-k
    sequence.append(sum_numbers(sequence,begin,i))
for i in sequence:
    print("{0} ".format(i),end='')