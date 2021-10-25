n = int(input())
a=[]

for _ in range(n):
    a.append(input())

count = 0

for i in range(n):
    group = []
    error = 0
    for x in range(len(a[i])) :
        if a[i][x] not in group :
            group.append(a[i][x])
        else :
            if a[i][x] == group[-1] :
                continue
            else :
                error += 1
    if error == 0 :
        count += 1

print(count)