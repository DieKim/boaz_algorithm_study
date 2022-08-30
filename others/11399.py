n = int(input())
p_li = list(map(int, input().split()))
tmp=0; res=[]
for p in sorted(p_li):
    tmp += p
    res.append(tmp)

print(sum(res))
