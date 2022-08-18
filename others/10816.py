n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

dic = {}
for n_ in n_list:
    try: 
        dic[n_] += 1
    except:
        dic[n_] = 1

for m_ in m_list:
    try:
        print(dic[m_], end=' ')
    except:
        print(0, end=' ')
    