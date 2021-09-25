def push(X):
    stack.append(X)
    return stack

import re

stack=[]
Order=[]

Order_num=int(input())

while Order_num>=1 :
    Order.append(input())
    Order_num -= 1

for i in Order :    
    if re.search(r"push \d+", i):
        match = re.search(r"push (\d+)", i)
        push(int(match.group(1)))
    elif i=="pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif i=="size":
        print(len(stack))
    elif i=="empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif i=="top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])

