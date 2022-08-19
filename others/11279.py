import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(heap, -x)
    else:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)