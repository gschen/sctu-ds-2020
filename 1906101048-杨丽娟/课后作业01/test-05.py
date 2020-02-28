L=[14,25,98,75,23,1,4,56,59]
n=int(input())
m=int(input())
a=L[n]
b=L[m]
L[m]=a
L[n]=b
print(L)