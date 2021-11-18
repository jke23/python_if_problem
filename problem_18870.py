from sys import stdin
a = int(stdin.readline())
num = list(map(int,stdin.readline().split()))
inde = list(num)
fin = []
inde.sort()
for i in range(a) :
    fin.append(inde.index(num[i]))

print(" ".join(map(str,fin)))