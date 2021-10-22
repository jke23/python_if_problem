a = int(input())

for _ in range(0,a):
    m, string = map(str,input().split())
    string_list = list(string.strip())
    print("".join(map(lambda x: x*int(m), string_list)))

