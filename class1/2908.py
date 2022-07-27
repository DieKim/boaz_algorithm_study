a, b = map(int, input().split())
li_a = list(reversed(str(a)))
re_a = int(''.join(li_a))
li_b = list(reversed(str(b)))
re_b = int(''.join(li_b))
if re_a > re_b:
    print(re_a)
else:
    print(re_b)