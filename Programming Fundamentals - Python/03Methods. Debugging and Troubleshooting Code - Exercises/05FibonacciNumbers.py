def fibonaci(number):
    f0 = 1
    f1 = 1
    for i in range (0,number-1):
        fnext = f0+f1
        f0 = f1
        f1 = fnext
    return f1

number = int(input())
print(fibonaci(number))