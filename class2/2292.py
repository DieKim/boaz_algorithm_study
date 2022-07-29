n = int(input())
if n==1:
    i=1
else:
    i=0
    while n>1:
        n -= i*6
        i += 1        
print(i)
