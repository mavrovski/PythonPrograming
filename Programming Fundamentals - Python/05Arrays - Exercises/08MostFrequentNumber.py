numbers = list(map(int,input().split()))

length = len(numbers)
counter = 0
best_counter = 0
most_frequent_number = 0

for i in range (length-1,-1,-1):
    for j in range (length-1,-1,-1):
        if numbers[i] == numbers [j]:
            counter +=1
        else:
            counter = 0
        if best_counter <= counter:
            most_frequent_number = numbers[i]
            best_counter = counter
print(most_frequent_number)