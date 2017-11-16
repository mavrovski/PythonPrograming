symbol = input()

try:
    int(symbol)
    print("digit")
except:
    if symbol == 'a' or symbol == 'e' or symbol == 'i' or symbol == 'o' or symbol == 'u':
        print("vowel")
    else:
        print("other")