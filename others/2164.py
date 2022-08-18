#덱: 양방향으로 넣고 뺄 수 있는 자료구조
from collections import deque

n = int(input())
deque = deque([i for i in range(1, n+1)])

while len(deque) > 1:
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])

# #리스트(시간초과)
# n = int(input())
# li = list(range(1, n+1))

# while len(li) != 1:
#     li.remove(li[0])
#     li.append(li[0])
#     li = li[1:]
    
# print(li[0])
