import sys
n = int(sys.stdin.readline())
n_set = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

for m in m_list:
    if m in n_set:
        print(1)
    else:
        print(0)
        
#받을 때부터 set으로 받아서 시간 단축하기
        