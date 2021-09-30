import sys

a, b = map(int,input().split())
coins=[int(sys.stdin.readline().strip()) for i in range(a)]
real_min_coin = 0

def coin_cal(coins,money,min_coin):
    global n
    if money > 1 :
        for n in range(len(coins)-1,-1,-1) :
            if money >= coins[n] :
                break
        min_coin += money//coins[n]
        coin_cal(coins,money%coins[n],min_coin)
    return min_coin


print(coin_cal(coins,b,real_min_coin))

