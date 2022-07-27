nums = [int(input()) for i in range(10)]
s = set()
for n in nums:
    s.update({n%42})
print(len(s))