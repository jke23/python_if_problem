from sys import stdin

a = [0]*10
number = str(stdin.readline().rstrip())

for x in range(len(number)):
    a[int(number[x])] += 1

string = ""
for i in range(len(a)-1,-1,-1) :
    if a[i] != 0 :
        string += str(i)*a[i]

print(string)