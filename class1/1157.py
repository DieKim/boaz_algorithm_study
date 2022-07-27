words = input().upper()
dic = dict()

for w in words:
    try:
        dic[w] += 1
    except:
        dic[w] = 1
    
if list(dic.values()).count(max(dic.values())) == 1:
    print(sorted(dic.items(), 
                 key=lambda item: item[1],
                 reverse=True)[0][0])
else:
    print('?')