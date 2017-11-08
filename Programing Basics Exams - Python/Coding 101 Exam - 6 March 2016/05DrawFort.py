n = int(input())

# top

mid = int(n / 2)
midSize = 2 * n - 2 * mid - 4

# bottom
if n <= 4:
    print("/{0}\\/{0}\\".format('^'*int(mid)))
else:
    print("/{0}\\{1}/{0}\\".format('^'*int(mid),'_'*int(midSize)))

if n <= 4:
    for i in range(0,n-2):
        print("|{0}|".format(' '*int(n*2-2)))
    print("\{0}/\{0}/".format('_'*int(mid)))
elif n>4:
    for i in range(0,n-3):
        print("|{0}|".format(' ' * int(2*n-2)))
    print("|{0}{1}{0}|".format(' ' * int(mid+1),'_' *int(midSize)))
    print("\{0}/{1}\{0}/".format('_'*int(mid),' '*int(midSize)))



