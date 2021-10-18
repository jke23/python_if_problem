from sys import stdin
Case = int(input())
Problem=[]
for _ in range(Case):
    Problem.append(str(input()))

for x in range(Case):
    Sum = 0
    i = 0
    for n in range(0,len(Problem[x])):
        if Problem[x][n] == "O" :
            i +=1
            Sum += i
        else :
            i = 0
            continue
    print(Sum)

