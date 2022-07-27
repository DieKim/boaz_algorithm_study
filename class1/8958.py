n = int(input())
ox_list = [input() for i in range(n)]
for ox in ox_list:
    res = 0
    oo = ox.split('X')
    for o in oo:
        try:
            for i in range(1, len(o)+1):
                res += i
        except:
            pass
    print(res)