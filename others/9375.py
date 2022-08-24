t = int(input())
for i in range(t):
    n = int(input())
    dic = {}
    for j in range(n):
        _, kind = input().split()
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1
    cnt=1
    for d in dic:
        cnt *= dic[d]+1
    print(cnt-1)





    