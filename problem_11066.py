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
    for n in range(1,File_num/2):
        Num=File_num//(2*n)
        if File_num%(2*n) == 0 :
            X_file.append(File_con(X,Num,Size_file))
        else :
            X_file.append(File_con(X,Num-1,Size_file))
            X_file.append(Size_file[-1])





