n = int(input())

s_li = []
for i in range(n):
    s = input()
    s_li.append(s)

res = []
for s in s_li:
    if s=='pop':
        try:
            print(res.pop(-1))
        except:
            print(-1)
    elif s=='size':
        print(len(res))
    elif s=='empty':
        if res==[]:
            print(1)
        else:
            print(0)
    elif s=='top':
        try:
            print(res[-1])
        except:
            print(-1)
    else:
        res.append(int(s.split()[1]))
