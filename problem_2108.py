a = int(input())

num = []
for _ in range(a) :
    num.append(int(input()))

num.sort()
coun = []
inde = []

for x in range(a):
    coun.append(num.count(num[x]))
if coun.count(max(coun)) > 1 :
    for i in range(a) :
        if coun[i] == max(coun) :
            if num[i] not in inde :
                inde.append(num[i])
inde.sort()
print(round(sum(num)/a))
print(num[int(a/2)])
print(inde[1])
print(num[-1]-num[0])