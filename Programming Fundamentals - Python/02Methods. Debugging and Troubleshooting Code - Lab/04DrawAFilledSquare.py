def print_top_and_bottom_row(n):
    print("-"*(2*n))

def print_middle_row(n):

    for j in range (0,n-2):
        print("-", end='')
        for i in range (0,n-1):
            print("\\/",end='')
        print("-")

def print_ticket(n):
    print_top_and_bottom_row(n)
    print_middle_row(n)
    print_top_and_bottom_row(n)

n=int(input())
print_ticket(n)