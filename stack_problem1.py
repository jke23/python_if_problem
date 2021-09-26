def push(X):
    stack.append(X)
    return stack

import re
import sys
stack=[]
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

for i in data :
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

