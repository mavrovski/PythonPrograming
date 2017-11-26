array = list(map(int,input().split(' ')))
rotate_times = int(input())
sum_arrays = [0]*len(array)

def rotate_array(arr):
    last_element = arr[len(arr)-1]
    for i in range (len(arr)-1,-1,-1):
        arr[i]=arr[i-1]
    arr[0]=last_element

for i in range (0,rotate_times):
    rotate_array(array)
    for j in range (0,len(array)):
        sum_arrays[j]+=array[j]

print(' '.join(list(map(str,sum_arrays))))


