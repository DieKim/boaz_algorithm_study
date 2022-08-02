n = int(input())
res = 0
for i in range(1, n+1):        
    n_li = list(map(int, str(i)))  
    n_tmp = i + sum(n_li)              
    if(n_tmp == n):                 
        res = i                   
        break
print(res)

#*