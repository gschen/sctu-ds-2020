#求给定数的阶乘
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。

list1=[1,10,20,30,40,50]
def yang(x):
    if x==0:
        return 1
    else:
        return x*yang(x-1)
while True:
    y=int(input())
    if y in list1 or y<0:
        break
    else:
        print(yang(y))  