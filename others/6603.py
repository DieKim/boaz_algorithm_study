def dfs(depth, idx):
    if depth == 6:
        print(*out)
        return
    for i in range(idx, k):
        out.append(li[i])
        dfs(depth+1, i+1)
        out.pop()

while True:
    li = list(map(int, input().split()))
    k = li.pop(0)
    if k==0:
        break
    out = []
    dfs(0, 0)
    print()

        