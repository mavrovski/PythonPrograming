c1 = input()
c2 = input()
c3 = input()
word = c1+c2+c3
# print(word[::-1])

wordReverse = ''
for i in range(len(word)-1,-1,-1):
    wordReverse+=word[i]
print(wordReverse)