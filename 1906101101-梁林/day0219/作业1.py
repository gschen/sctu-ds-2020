#1、求给定数的阶乘 
#定数：19
x=1
for i in range(1,20):
    x*=i 
print(x) 

#第二题
P,T,R=map(int,input().split(' '))
print(P*T*R/100)

#第三题
a=[14,25,98,75,23,1,4,56,59]
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        a[i+1]=a[i]
print(a[i+1])

#第四题
b=[14,25,98,75,23,1,4,56,59]
n=int(input())
if n>len(b):
    print('索引超出范围')
b=b[:n]
z=0
for i in b:
    z+=i**2
print(z)

#第五题
n1,n2=map(int,input().split(' '))
d=[14,25,98,75,23,1,4,56,59]
if n1>len(d) or n2>len(d):
    print('索引超出范围')
d[n1],d[n2]=d[n2],d[n1]
print(d)