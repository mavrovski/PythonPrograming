def print_sign(n):
    if n > 0:
        print("The number %d is positive." %n)
    elif n == 0:
        print("The number %d is zero." % n)
    elif n < 0:
        print("The number %d is negative." % n)

n = int(input())
print_sign(n)