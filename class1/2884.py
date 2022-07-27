hh, mm = map(int, input().split())
if mm >= 45:
    print(hh, mm-45)
else:
    if hh-1<0:
        print(23, 60-45+mm)
    else:
        print(hh-1, 60-45+mm)