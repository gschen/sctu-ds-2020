#求给定数的阶乘
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。

list0=[1,10,20,30,40,50]
def yang(a):
    if a==0:
        return 1
    else:
        return a*yang(a-1)
while True:
    b=int(input())
    if b in list0 or b<0:
        break
    else:
        print(yang(b))    