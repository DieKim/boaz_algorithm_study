n_list = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        n_list.append(n)
    
for n in n_list:
    n_li = list(str(n))
    n_li.reverse()
    if list(str(n)) == n_li:
        print('yes')
    else:
        print('no')
