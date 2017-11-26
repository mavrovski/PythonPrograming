array = list(map(int,input().split(' ')))
k = int(len(array)/4)

left_array = [0]*k
middle_array = [0]*2*k
right_array = [0]*k
array_results = [0]*2*k

for i in range (0,k):
    left_array[i]=array[i]
    right_array[i]=array[3*k+i]

for i in range (0,2*k):
    middle_array[i]=array[k+i]


left_array.reverse()
right_array.reverse()

for i in range (0,k):
    array_results[i] += middle_array[i]+left_array[i]
    array_results[i+k]=middle_array[i+k]+right_array[i]

print(' '.join(map(str,array_results)))