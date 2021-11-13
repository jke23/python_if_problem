import heapq
from sys import stdin
a = int(stdin.readline())
heap=[]
for _ in range(0,a):
    i = int(stdin.readline())
    heapq.heappush(heap,i)

for x in range(a):
    print(heapq.heappop(heap))