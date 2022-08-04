n, m = map(int, input().split())
no_li = {input() for i in range(n)}
no_se = {input() for i in range(m)}
no_all = sorted(list(no_li.intersection(no_se)))
print(len(no_all))
for no in no_all:
    print(no)