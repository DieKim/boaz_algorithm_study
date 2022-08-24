n = int(input())

tmp = 1
for i in range(1, n+1):
    tmp *= i

res = 0
for j in str(tmp)[::-1]:
    if j=='0':
        res += 1
    else:
        break

print(res)