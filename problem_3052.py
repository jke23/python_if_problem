num=[]
for _ in range(10) :
    num.append(int(input()))
left_num = []

for i in range(0,10):
    if num[i]%42 not in left_num :
        left_num.append(num[i]%42)
    else :
        continue

print(len(left_num))