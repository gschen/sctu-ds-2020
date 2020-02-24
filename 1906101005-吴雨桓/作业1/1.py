x=int(input())
l=[1,10,20,30,40,50]

def wu(x):
    if x!=0:
        return x*wu(x-1)
    else:
        return 1

    

if x in l:
    print('请重新输入')
else:
    print(wu(x))