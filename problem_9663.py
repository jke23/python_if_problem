a = int(input())

chess = [[0]*a]*a

def chess_not_queen(N, X, chess) :
    chess[N][X] = 1
    chess[N] = 1
    chess[:][X] = 1
    for i in range(X + 1,len(chess)):
        y = 0
        chess[i][y] = 1
        chess[-i][y]
        chess[i][-y]
        chess[-i][-y]
        y += 1







