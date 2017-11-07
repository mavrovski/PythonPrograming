n = int(input())
firstLastRow = "+ "+ str('- ')*(n-2)+"+"
middleRows = "| "+ str('- ')*(n-2)+"|"
print(firstLastRow)
for i in range(0,n-2):
    print(middleRows)
print(firstLastRow)