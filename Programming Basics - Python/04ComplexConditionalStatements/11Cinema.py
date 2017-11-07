typeOfTicket = input().lower()
rows = int(input())
columns = int(input())

premiere = 12.00
normal = 7.50
discount = 5.00
result = 0.00
if typeOfTicket == "premiere":
    result = rows*columns*premiere
elif typeOfTicket == "normal":
    result = rows*columns*normal
elif typeOfTicket == "discount":
    result = rows*columns*discount
print("{0:.2f}".format(result))