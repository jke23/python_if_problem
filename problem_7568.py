from sys import stdin
i = int(input())

human = [list(map(int,stdin.readline().split()))for _ in range(i)]

first = 0
count = 0

print(human)
for x in range(i) :
    for y in range(x,i+1):
        if human[x][0] > human[y][0] :
            if human[x][1] > human[y][1] :
                first = x
            else :
                count += 1