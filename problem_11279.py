import heapq
from sys import stdin
a = int(stdin.readline())
heap=[]
for _ in range(0,a):
    i = int(stdin.readline())
    if i == 0:
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print("0")
    else :
        heapq.heappush(heap,(-i,i))