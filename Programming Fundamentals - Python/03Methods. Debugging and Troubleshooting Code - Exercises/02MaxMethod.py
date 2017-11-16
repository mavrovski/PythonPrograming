def max_function(a,b):
   return max(a,b)

a = int(input())
b = int(input())
c = int(input())

print(max_function(a,max_function(b,c)))
