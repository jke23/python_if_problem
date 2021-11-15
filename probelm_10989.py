from sys import stdin

a = int(input())
A = []
for _ in range(a) :
    i = int(input())
    A.append(i)

count = [0]*(a+1)
countSum = [0]*(a+1)

for i in range(0, a):
    count[A[i]] += 1

countSum[0] = count[0]
for i in range(1, a+1):
    countSum[i] = countSum[i-1]+count[i]

B = [0]*(a+1)
for i in range(a-1, -1, -1):
    B[countSum[A[i]]] = A[i]
    countSum[A[i]] -= 1


for i in range(1,a+1):
    print(B[i])



