#求给定数的阶乘
#要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。

num=int(input("输入你所求的阶乘数："))
i=1
if num>0:
    if num>0 and num<=50:
        if num!=1 and num%10==0:
            print("不满足要求")
        else:
            for a in range(1,num+1):
                i=i*a
            print("%d的阶乘为%d"%(num,i))
    else:
        for a in range(1,num+1):
            i=i*a
        print("%d的阶乘为%d"%(num,i))
elif num<0:        
    print("负数没有阶乘")
else:
    print("0的阶乘为1")