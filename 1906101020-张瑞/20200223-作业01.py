#1
a=int(input('输入数字：'))
l=[1,10,20,30,40,50]
n,s =1,a
if a not in l:
    if a==0:
        print('阶乘是：1')
    else:     
         while n<a:
            for x in range(1,a):
                s=s*x
                n=n+1        
            print('阶乘是：%s'%(s))
else:
    print('该数字不在计算范围内')
#2
P=int(input('本金(P)：'))
R=int(input('利率(R)：'))
T=int(input('时间(T)：'))
D=(P*T*R)/100
print('单利为:%d'%(D))
#3
list=[14,25,98,75,23,1,4,56,59]
list.sort()
print('最大元素：',list[-1])
#4
n=int(input('输入数字:'))
b,s=n,0
if n>10:
    print('超出范围')
else:
    while n>0:
        x=(14,25,98,75,23,1,4,56,59)
        s=pow(x[n-1],2)+s
        n=n-1
    print('前%d个数的平方和为：%d'%(b,s))
#5
a=int(input('输入想交换的第一个位置：'))
b=int(input('输入想交换的第二个位置：'))
x=[14,25,98,75,23,1,4,56,59]
c=pow(x[b-1],2)
x[b-1]=x[a-1]
x[a-1]=round(pow(c,0.5))
print(x)