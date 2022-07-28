n = int(input())
words = [input() for i in range(n)]
li = []

for w in set(words):
    li.append([len(w), w])
    
for i in sorted(li):
    print(i[1])
