a, b, c = [int(input()) for i in range(3)]
abc = a*b*c
dic = dict()

for i in str(abc):
    try:
        dic[i] += 1
    except:
        dic[i] = 1

for i in range(10):
    try: 
        print(dic[str(i)])
    except:
        print(0)