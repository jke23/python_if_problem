from sys import stdin
from functools import reduce

a = int(input())

for x in range(a):
    Case = list(map(int, stdin.readline().split()))
    Sum_score = reduce(lambda x,y : x+y, Case[1:])
    Standard_score = Sum_score/Case[0]
    Upper = 0
    for i in range(1,Case[0]+1):
        if Case[i] > Standard_score :
            Upper += 1
        else :
            continue
    print("{:.3f}%".format(Upper/Case[0]*100))
