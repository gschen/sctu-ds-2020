n=int(input("please enter:"))
m=1
if n == 0:
    print("0的阶乘为1")
if n < 0:
    print("负数没有阶乘")
else:
    for i in range(1,n+1):
        m = m*i
print("%d的阶乘是%d" % (n,m))