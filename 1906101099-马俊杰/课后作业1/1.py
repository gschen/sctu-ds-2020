#1、	求给定数的阶乘
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]

a = int(input())
x = 1                   
y=[1,10,20,30,40,50]
if a == 0:
    print(0)
if a < 0:
    print('error')    
if a > 0:
    if a in y:
        print('error')
    else:
        for  i in range(1,a+1):    
            x *= i              
        print(x)