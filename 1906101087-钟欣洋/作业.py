#第一题 求给定数的阶乘
def jiecheng(a):
    if a==0 or a==1:
        return 1
    else:
        return (a*jiecheng(a-1))
asm=jiecheng(5) 
print(asm)       

#第二题 求单利
P,T,R=map(int,input("请输入以空格相隔开的P，T，R").split())
print((P*T*R)/100)

#第三题 找最大数
a=0
for i in [14,25,98,75,23,1,4,56,59]:
    if i>a:
        a=i
print(a) 



#第四题 求指定数的平方
old=[14,25,98,75,23,1,4,56,59]
a=[i*i for i in old]
o=0
n=int(input("Please enter a positive integer less than Ten:"))
for q in a:
    while n>0:
        o=a[n-1]+o
        n=n-1
print(o)

#第五题 指定数字交换位置
last=[14,25,98,75,23,1,4,56,59]
n=int(input("请输入您要交换的数字的位置一："))
m=int(input("请输入您要交换的数字的位置二："))
last[n-1],last[m-1]=last[m-1],last[n-1]
print(last)
