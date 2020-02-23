n=int(input("请输入一个整数:"))
s=1
L=[1,10,20,30,40,50]
if n in L:
    print("错误,不能计算该数的阶乘")
else:
    for i in range(1,n+1):
        s=s*i
        print(s)
