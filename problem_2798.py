import sys
a, b = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))

card_sum=[]

for n in range(0,a-2) :
    for i in range(n+1,a-1):
        for x in range(i+1,a):
            if card[n]+card[i]+card[x] not in card_sum :
                card_sum.append(card[n]+card[i]+card[x])
distance = 1000
index_num = 0
for y in range(0,len(card_sum)) :
    if distance > abs(b-card_sum[y]) :
        distance = abs(b - card_sum[y])
        index_num=y

print(card_sum[index_num])