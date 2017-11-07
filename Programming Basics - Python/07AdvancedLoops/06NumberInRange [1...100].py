n=int(input("Еnter a number in the range [1...100]:"))

while(n>100 or n<=0):
    print("Invalid number!")
    n = int(input("Еnter a number in the range [1...100]:"))
print("The number is: %d" %n)
