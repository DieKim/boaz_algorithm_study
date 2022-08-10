n = int(input())
li = [i for i in range(1, n+1)]
while len(li) > 1:
    print(li.pop(0), end=' ')
    li.append(li.pop(0))
print(li[0], end=' ')
    
    