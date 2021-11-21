a = int(input())
#0은 none
#1은 queen
#2는 false
chess = [[0]*a]*a
for i in range(a):
    for x in range(a) :
        chess[i][a] = 1
        chess[i][:a] = 2
        chess[i][a+1:] = 2
        chess[i+1:][a] = 2

