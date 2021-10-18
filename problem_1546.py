from sys import stdin
from functools import reduce

a = int(input())
Score = list(map(int,stdin.readline().split()))
Score.sort()
large_score = Score[-1]
Med_score=0
for i in range(0,a):
    Med_score += Score[i]/large_score*100

print(Med_score/a)