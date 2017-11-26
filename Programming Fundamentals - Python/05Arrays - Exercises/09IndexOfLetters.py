alphabet = [  'a', 'b', 'c', 'd' ,'e',
                'f', 'g', 'h', 'i' ,'j',
                'k', 'l', 'm', 'n' ,'o',
                'p', 'q', 'r', 's' ,'t',
                'u', 'v', 'w', 'x', 'y',
                'z']
word = input().lower()

word_length = len(word)
alphabet_length = len(alphabet)

for i in range (0,word_length):
    for j in range (0,alphabet_length):
        if word[i]==alphabet[j]:
            print("{0} -> {1}".format(word[i],j))
