array = input().split(' ')
array_to_int = list(map(int,array))
match = False
for a in range (0,len(array_to_int)):
    for b in range (a+1,len(array_to_int)):
        sum = array_to_int[a]+array_to_int[b]
        if array_to_int.__contains__(sum):
            print("{0} + {1} == {2}".format(array_to_int[a],array_to_int[b],sum))
            match = True
if match == False:
    print("No")