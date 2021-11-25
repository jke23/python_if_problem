def File_con(List,Num,Size_file):
    for n in range(0,Num,2):
        List.append(Size_file[n]+Size_file[n+1])
    return List

from sys import stdin

Test_num = int(stdin.readline())

X_file = []
X = []
for i in range(Test_num) :
    File_num = int(stdin.readline())
    Size_file = list(map(int,stdin.readline().split()))






