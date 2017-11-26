numbers = list(map(int,input().split()))

length = len(numbers)

for i in range (0,length):
    left_sum = 0
    right_sum = 0

    for j in range (0,i):
        left_sum+=numbers[j]

    for j in range (i+1,length):
        right_sum+=numbers[j]

    if left_sum == right_sum:
        print(i)
        exit()
print("no")
