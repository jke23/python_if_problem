a = int(input())


for x in range(1,a) :
    num = []
    med_num = str(x)
    for i in range(len(med_num)):
        num.append(int(med_num[i]))
    #print(num)
    number_sum = x + sum(num)
    if number_sum == a :
        print(x)
        break
    else :
        continue