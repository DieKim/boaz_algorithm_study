n, k = map(int, input().split())
up = 1
down = 1
for i in range(k):  
    up *= n
    down *= (k-i)
    n -= 1
print(int(up/down))