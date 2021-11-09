def make_chess(chess) :
    count = 0
    wb = 0
    if chess[0][0] == "W" :
        for y in range(8):
            wb += 1
            for x in range(8) :
                wb += 1
                if wb%2 == 0 :
                    color = "W"
                else :
                    color = "B"
                if chess[y][x] != color :
                    chess[y][x] = color
                    count += 1
    else :
        for y in range(8):
            wb += 1
            for x in range(8):
                wb += 1
                if wb % 2 == 0:
                    color = "B"
                else:
                    color = "W"
                if chess[y][x] != color:
                    chess[y][x] = color
                    count += 1
    return count, chess
from sys import stdin

m, n = map(int, stdin.readline().split())

r_plate = [list(map(str, stdin.readline().strip())) for _ in range(m)]

med_chess = []
min_count = 10000
for i in range(m-7) :
    for x in range(n-7):
        for y in range(i,i+8) :
            med_chess.append(r_plate[y][x:x+8])
        count, chess = make_chess(med_chess)
        print(chess)
        print(count)
        if min_count > count :
            min_count = count
        med_chess = []

print(min_count)
