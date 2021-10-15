a = int(input())
Num_split=[]
med_a=[]
if a<10 :
    a=a*10

for x in map(int, str(a)):
    med_a.append(x)

Num_split.append(med_a)

i=0
if a !=0 :
    while True :
        Sum = Num_split[i][0] + Num_split[i][1]
        med_sum=[]
        for n in map(int, str(Sum)):
            med_sum.append(n)
        Num_split.append([Num_split[i][1],med_sum[-1]])
        i += 1
        if Num_split[-1] == Num_split[0] :
            break
        else :
            continue
    print(i)
else :
    print("1")
