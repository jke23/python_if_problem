import sys
a, b = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))

card_sum=[]

for n in range(0,a-2) :
    for i in range(n+1,a-1):
        for x in range(n+2,a):
            card_sum.append(card[n]+card[i]+card[x])

