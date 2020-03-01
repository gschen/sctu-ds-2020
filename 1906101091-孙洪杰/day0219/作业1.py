#1
x=1
y=int(input("给定数"))
for i in range(1,y+1):
    x=x*i
    print(x)


#2
P=int(input("输入本金"))
R=int(input("输入利率"))
T=int(input("输入时间"))
print((P*T*R)/100)


#3
list=[14,25,98,75,23,1,4,56,59]
print(max(list))

#法二
list=[14,25,98,75,23,1,4,56,59]
list.sort()
print(list[-1])

#4
L=[14,25,98,75,23,1,4,56,59]
n=int(input())
sum=0
for x in range(0,n):
    a=list[x]**2
    sum=sum+a
print(sum)

#5
L=[14,25,98,75,23,1,4,56,59]
a=int(input())
b=int(input())
i=L.index("a")
j=L.index("b")
L[i],L[j]=L[j],L[i]
print(L)