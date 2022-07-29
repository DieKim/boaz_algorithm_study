n = int(input())
li = [input().split() for i in range(n)]
li.sort(key=lambda x: int(x[0]))
for i in li:
    print(i[0], i[1])
