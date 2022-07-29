n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
li.sort()
li.sort(key=lambda x: x[1])
for i in li:
    print(i[0], i[1])
    
