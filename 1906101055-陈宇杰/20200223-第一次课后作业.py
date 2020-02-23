#第一题
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


#第二题
p=int(input())
t=int(input())
r=int(input())
m = (p*t*r)/100
print(m)


#第三题
L=[14,25,98,75,23,1,4,56,59]
L.sort()
print(L[-1])




#第四题
L=[14,25,98,75,23,1,4,56,59]
n=int(input())
m=list(L[:n])
s=0
for i in m:
    s=s+i**2
print(s)



#第五题
import random
L=[14,25,98,75,23,1,4,46,59]
n=int(input())
m=int(input())
a=random.randint(1,len(L))
b=random.randint(1,len(L))
L[a]=n
L[b]=m
print(L)