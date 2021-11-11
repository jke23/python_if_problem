def make_chess(chess) :
    mini = []
    count = 0
    wb = 0
    for y in range(8):
        wb += 1
        for x in range(8) :
            wb += 1
            if wb%2 == 0 :
                color = "W"
            else :
                color = "B"
            if chess[y][x] != color :
                count += 1
    mini.append(count)
    wb = 0
    count =0
    for z in range(8):
        wb += 1
        for i in range(8):
            wb += 1
            if wb % 2 == 0:
                color = "B"
            else:
                color = "W"
            if chess[z][i] != color :
                count += 1
    mini.append(count)
    return min(mini)
from sys import stdin

m, n = map(int, stdin.readline().split())

r_plate = [list(map(str, stdin.readline().strip())) for _ in range(m)]

med_chess = []
min_count = 10000
for i in range(m-7) :
    for x in range(n-7):
        for y in range(i,i+8) :
            med_chess.append(r_plate[y][x:x+8])
        count = make_chess(med_chess)
        if min_count > count :
            min_count = count
        med_chess = []

print(min_count)
