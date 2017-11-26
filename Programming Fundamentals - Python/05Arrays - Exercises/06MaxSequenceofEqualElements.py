array = list(map(int,input().split(' ')))

start_index = 0
sequance_length = 1

best_start_index = 0
best_sequance_length = 0

for i in range (0,len(array)):
    if array[i]==array[i-1]:
        sequance_length+=1
        if sequance_length>best_sequance_length:
            best_start_index = start_index
            best_sequance_length = sequance_length

    else:
        start_index = i
        sequance_length = 1

for i in range (best_start_index,best_start_index+best_sequance_length):
    print("{0} ".format(array[i]),end='')