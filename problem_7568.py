from sys import stdin
i = int(input())

human = [list(map(int,stdin.readline().split()))for _ in range(i)]
grade = []

count = 0

for x in range(i) :
    count = 1
    for y in range(i):
        if human[x][0] < human[y][0] :
            if human[x][1] < human[y][1] :
                count += 1
            else :
                continue
    grade.append(count)

print(" ".join(map(str,grade)))