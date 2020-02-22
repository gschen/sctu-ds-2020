# 求给定数的阶乘
x=1
s=int(input("给定数为："))
if s==1 or s==10 or s==20 or s==30 or s==40 or s==50:
    raise ValueError
else:
    for i in range(1,s+1):
        x=x*i
        print(x)
#第二题
P=int(input("P="))
T=int(intput("T="))
R=int(intput("R="))
S=(P*T*R)/100
print('%d'%s)
#第三题
lis1=[14,25,98,75,23,1,4,56,59]
print(max(lis1))
#第四题
s=0
n=int(input())
lis2=[14,25,98,75,23,1,4,56,59]
if n>len(lis2):
    print('n大于数组长度')
else:
    for i in lis2[:n]:
        s=s+i**2
    print(s)
#第五题
lis3=[14,25,98,75,23,1,4,56,59]
x,s=map(int,input("输入两个置换元素的位置： ".split(',')))
b=lis3[x]
lis3[x]=lis3[s]
lis3[s]=b
print(lis3)


