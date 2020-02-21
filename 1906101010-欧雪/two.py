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


