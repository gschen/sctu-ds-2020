#1
m=int(input("请输入一个数:"))
n=1
if m == 0:
    print("阶乘为1")
if m < 0:
    print("该数没有阶乘")
if m == 1 or m ==10 or m ==20 or m ==30 or m ==40 or m ==50:
    pass
else:
    for i in range(1,n+1):
        m = m*i
        print(m)


#2
P=int(input())
T=int(input())
R=int(input())
n = (P*T*R)/100
print(n) 


#3
list=[14,25,98,75,23,1,4,56,59]
print(max(list))


#4
list=[14,25,98,75,23,1,4,56,59]
n=int(input())
s=0
if n<len(list):
    while n>0:
        s=s+list[n-1]**2
        n-=1
print(s)


#5.list=[14,25,98,75,23,1,4,56,59]
m,n=map(int,input('输入两个置换元素的位置').split(','))
a=list[m]
list[m]=list[n]
list[n]=a
print(list)