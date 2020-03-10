#第一题
num=int(input("你所求的阶乘数："))
i=1
if num>0:
    if num>0 and num<=50:
        if num!=1 and num%10==0:
            print("error")
        else:
            for a in range(1,num+1):
                i=i*a
            print("%d的阶乘为%d"%(num,i))
    else:
        for a in range(1,num+1):
            i=i*a
        print("%d的阶乘为%d"%(num,i))
if num<0:        
    print("负数没有阶乘")
if num==0:
    print("0的阶乘为1")


#第二题
P=float(input("P="))
R=float(input("R="))
T=float(input("T="))
danli=(P+T+R)/100
print(danli)

#第三题
lis1=[14,25,98,75,23,1,4,56,59]
print(max(lis1))

#第四题
lis1=[14,25,98,75,23,1,4,56,59]
n=int(input("输入n:"))
a=len(lis1)
if n>a or n<1:
    print("error")
else:
    b=0
    while n>=1:
        b+=lis1[n-1]**2
        n=n-1
    print(b)

#第五题
lis1=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input("输入需要交换的位置：").split())
lis1[a],lis1[b]=lis1[b],lis1[a]
print(lis1)










