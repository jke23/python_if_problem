from sys import stdin
num = []
a = int(stdin.readline())
for n in range(a) :
    num.append(int(stdin.readline()))
num.sort()


check_list = [0] * 8001
for i in range(a):
    check_list[4000+num[i]] += 1
count = 0
maximum = max(check_list)
if check_list.count(maximum) > 1:
    for x in range(8002) :
        if check_list[x] == maximum :
            count += 1
            second_num = x - 4000
            if count > 1 :
                break
elif check_list.count(maximum) == 1 :
    second_num = check_list.index(max(check_list)) - 4000

print(round(sum(num)/a))
print(num[int(a/2)])
print(second_num)
print(num[-1]-num[0])