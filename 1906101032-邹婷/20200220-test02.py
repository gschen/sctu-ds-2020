#第一题
def factorial(n):
    result=n 
    for i in range (1,n):
        result *= i 
    return result
print (factorial(18))
#第二题
def addMulti(P,T,R):
    return (P*T*R)/100
print(addMulti(20000,10,10))

#第三题
from random import*
list=[14,25,98,75,23,1,4,56,59]
list.sort()
print(list)
print(list[-1])

#第四题
list1=[14,25,98,75,23,1,4,56,59]
x=int(input())
if 1<=x<=9:
    sum=0
    for i in list1[:x]:
        sum=sum+i*i
    print(sum)

#第五题
list2=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input().split())
list2[a],list2[b]=list2[b],list2[a]
print(list2)