import sys

a, b = map(int,input().split())
coins=[map(int,sys.stdin.readline(a))]
print(coins)
real_min_coin = 0
def coin_cal(coins,money,min_coin):
    if money > 1 :
        for n in range(len(coins)-1,-1,-1) :
            if money//coins[n] >=1 :
                min_coin +=1
                coin_cal(coins,money%coins[n],min_coin)
    elif min_coin == 1 :
        min_coin+=1
        return min_coin
    return min_coin

i=1
print(coin_cal(coins,b,real_min_coin))

