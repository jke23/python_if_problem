def next_num(number,len_num,k):
    for i in range(len_num-1,-1,-1) :
        if num[i] < k :
            num[i] = num[i]+1
            return num
        num[i] = 1
    return num

a, b = map(int,input().split())
num=[1 for _ in range(b)]
i=1
n=0
while i>0 :
    if num[0] == num[1] == num[2] :
        print(num[0],num[1],sep=' ')
    num=next_num(num,b,a)
    if num == [1 for _ in range(b)] :
        break