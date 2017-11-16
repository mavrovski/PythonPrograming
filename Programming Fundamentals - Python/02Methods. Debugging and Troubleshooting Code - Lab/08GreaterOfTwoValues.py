type = input()


def get_max(first, second):
    if first>=second:
       return first
    else:
        return second

if type == "int":
    first = int(input())
    second = int(input())
    maximum = get_max(first,second)
    print(maximum)

elif type == "char":
    first = input()
    second = input()
    maximum = get_max(first, second)
    print(maximum)

elif type == "string":
    first = input()
    second = input()
    maximum = get_max(first, second)
    print(maximum)
