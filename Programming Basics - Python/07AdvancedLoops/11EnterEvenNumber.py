n = int
while (bool):
    try:
        n = int(input("Enter even number:"))
        if n % 2 == 0:
            break
        print("The number is not even.")
    except:
        print("Invalid number!")
print("Even number entered: {0}".format(n))
