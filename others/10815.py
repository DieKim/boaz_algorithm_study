n = int(input())
n_li = set(map(int, input().split()))
m = int(input())
m_li = list(map(int, input().split()))
for m in m_li:
    if m in n_li:
        print(1, end=' ')
    else: 
        print(0, end=' ')
        