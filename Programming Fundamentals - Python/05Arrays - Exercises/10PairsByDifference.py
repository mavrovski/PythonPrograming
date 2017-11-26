numbers = list(map(int,input().split()))
diff = int(input())

length = len(numbers)
counter = 0

for i in range (0,length):
    for j in range (i,length):
        current_diff = abs(numbers[i]-numbers[j])
        if current_diff == diff:
            counter+=1

print(counter)