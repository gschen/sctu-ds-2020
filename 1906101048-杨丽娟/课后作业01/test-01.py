a=int(input("请输入一个数:"))
n=1
if a == 0:
    print("阶乘为1")
if a < 0:
    print("该数没有阶乘")
if a == 1 or a ==10 or a ==20 or a ==30 or a ==40 or a ==50:
    pass
else:
    for i in range(1,n+1):
        a = a*i
        print(a)


