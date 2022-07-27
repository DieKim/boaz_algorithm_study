n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
li.sort()
for i in li:
    print(i[0], i[1])