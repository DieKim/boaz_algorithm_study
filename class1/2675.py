t = int(input())
cases = [input().split() for i in range(t)]
for case in cases:
    for c in case[1]:
        print(c*int(case[0]), end='')
    print()