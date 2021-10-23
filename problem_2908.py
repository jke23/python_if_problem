a, b = list(map(int,input().strip().split()))
a = a.reverse()
b = b.reverse()
num_1=0
num_2=0
for i in range(0,3):
    num_1 += int(a[i])*10^(3-i)
for n in range(0,3):
    num_2 += int(b[n])*10^(3-n)

if num_1 > num_2 :
    print(num_1)
else :
    print(num_2)

'''
a = map(int,reversed(a))
b =map(int,reversed(b))
print(a,b)
if a > b :
    print(a)
else :
    print(b)
'''
