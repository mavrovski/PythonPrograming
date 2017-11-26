numbers = list(map(int,input().split(' ')))

length = len(numbers)
counter = 1
best_counter = 0
best_start = 0

for i in range (length-1,0,-1):
    if numbers[i]>numbers[i-1]:
        counter+=1
    else:
        counter = 1
    if best_counter<counter:
        best_start = i-1
        best_counter = counter
for i in range (best_start,best_start+best_counter):
    print("{0} ".format(numbers[i]),end='')
print()
