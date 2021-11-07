a = int(input())
true = [True]

for x in range(1,a) :
    num = []
    med_num = str(x)
    for i in range(len(med_num)):
        num.append(int(med_num[i]))
    number_sum = x + sum(num)
    if number_sum == a :
        print(x)
        true[0] = False
        break
    else :
        continue
if true[0] == True :
    print("0")