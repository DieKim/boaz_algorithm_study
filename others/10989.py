import sysinput = sys.stdin.readlinen = int(input())n_li = [0] * 10001for _ in range(n):    idx = int(input())    n_li[idx] += 1for i in range(10001):    if n_li[i] != 0:        for j in range(n_li[i]):            print(i)    