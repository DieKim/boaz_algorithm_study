import sys
input = sys.stdin.readline
n, k = map(int, input().split())
up=1; down=1
for i in range(k):
    up *= n
    down *= k
    n -= 1
    k -= 1
print((up//down)%10007)
