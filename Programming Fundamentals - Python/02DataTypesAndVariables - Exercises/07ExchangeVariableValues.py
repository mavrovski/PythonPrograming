a = int(input())
b =int(input())
print("Before:")
print("a = "+str(a))
print("b = "+str(b))
oldA = a
a = b
b = oldA
print("After:")
print("a = "+str(a))
print("b = "+str(b))