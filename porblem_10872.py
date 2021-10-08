a= int(input())

def factorial(n) :
    if n>1:
        fac_num = n*factorial(n-1)
        return fac_num
    else :
        return 1

print(factorial(a))