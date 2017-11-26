
array_one = list(map(int,input().split(' ')))
length = len(array_one)

if len(array_one) == 1:
    print("{ %g }" % (array_one[0]))
elif length % 2 == 0:

    print("{ %g, %g }" % (array_one[int(length/2-1)],array_one[int(length/2)]))
else:
    print("{ %g, %g, %g }" % (array_one[int(length/2-1)],array_one[int(length/2)],array_one[int(length/2+1)]))
