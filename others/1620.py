import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for idx in range(1, n+1):
    tmp = input().strip()
    dic[idx] = tmp
    dic[tmp] = idx
for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(dic[int(q)])
    else:
        print(dic[q])
        
#strip 유무 차이??

