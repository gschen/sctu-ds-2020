#第一题
# def factorial(n):
#     result=n 
#     for i in range (1,n):
#         result *= i 
#     return result
# print (factorial(18))
n=int(input('n='))
for i in range (1,n+1):
    n *= i
print(n)       
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
x=int(input('x='))
list1=list1[:x]
sum=0
for i in list1:
    if x>0:
        sum += i*i       
print(sum)

#第五题
list2=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input().split())
list2[a],list2[b]=list2[b],list2[a]
print(list2)