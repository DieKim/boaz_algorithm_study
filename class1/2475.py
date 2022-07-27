n = list(map(int, input().split()))
n2 = [i**2 for i in n]
print(sum(n2)%10)