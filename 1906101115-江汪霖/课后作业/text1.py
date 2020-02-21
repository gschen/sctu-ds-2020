n=int(input('请输入一个数：'))
m = 1
a=[1,10,20,30,40,50]
if n == 0:
    print("0的阶乘是0")
if n < 0:
    print("没有阶乘")
if n > 0 :
    if n in a :
        print("输入的数无效")
    else:
        for  i in range(1,n+1):
            m = m * i
        print("%d的阶乘等于%d"%(n,m))