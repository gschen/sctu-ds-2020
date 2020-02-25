x = int(input())
list = [1,10,20,30,40,50]
def num(x):
    if x == 0:
        return 1
    else:
        return x*num(x-1)
if x in list:
    print('错误')
else:
    print(num(x))