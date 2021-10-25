a = int(input())
i=0
num = 1

while True :
    if num >= a :
        break
    i += 1
    num += 6 * i
print(i+1)
