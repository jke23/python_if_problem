def make_chess(chess) :
    count = 0
    wb = -1
    if chess[0][0] == "W" :
        for y in range(8):
            wb += 1
            for x in range(8) :
                #wb += 1
                print("recall")
                print(wb)
                if wb%2 == 0 :
                    color = "W"
                else :
                    color = "B"
                if chess[y][x] != color :
                    chess[y][x] = color
                    count += 1
                wb += 1

    else :
        color = "B"
        for y in range(8):
            if color != "B":
                color = "B"
            else:
                color = "W"
            for x in range(8) :
                #print(x)
                if color == "B" :
                    color = "W"
                else :
                    color = "B"
                if chess[y][x] != color :
                    chess[y][x] = color
                    count += 1
                else :
                    continue
                print(chess[y][x])
    return count, chess

chess = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
print(make_chess(chess))