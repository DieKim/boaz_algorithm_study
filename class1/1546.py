n = int(input())
li = list(map(int, input().split()))
M = max(li)
li2 = []
for i in li:
    li2.append(i/M*100)
print(sum(li2)/n)