n, m = map(int, input().split())
p00, p01, p10, p11 = map(float, input().split())
p0 = [1-m]
p1 = [m]
for i in range(n):
    p0.append(p0[i]*p00+p1[i]*p10)
    p1.append(p0[i]*p01+p1[i]*p11)    

print(round(p0[-1]*1000))
print(round(p1[-1]*1000))