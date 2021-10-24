dial_num = {('a','b','c'):2,('d','e','f'):3,('g','h','i'):4,('j','k','l'):5,('m','n','o'):6,('p','q','r','s'):7,('t','u','v'):8,('w','x','y','z'):9}

a = list(map(str,input().strip()))
print(dial_num['a'])
count=0
'''
for i in range(len(a)):
    count += int(dial_num[a[i].lower()])+1

print(count)
'''