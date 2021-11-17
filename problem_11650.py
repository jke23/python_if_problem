from sys import stdin

a = int(stdin.readline())
x_y_list = [list(map(int,stdin.readline().split()))for _ in range(a)]
final = [0]*a

for x in range(a) :
    count = 0
    for y in range(a) :
        if x_y_list[x][0] > x_y_list[y][0] :
            count += 1
        elif x_y_list[x][0] == x_y_list[y][0] :
            if x_y_list[x][1] > x_y_list[y][1] :
                count += 1
    final[count] = x_y_list[x]
for n in range(a):
    print(" ".join(map(str,final[n])))