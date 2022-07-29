k = int(input())
n_list = []
for i in range(k):
    n = int(input())
    if n != 0:
        n_list.append(n)
    else:
        n_list.pop(-1)

print(sum(n_list))
