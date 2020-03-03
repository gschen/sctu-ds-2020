l=[14,25,98,75,23,1,4,56,59]
n=int(input("1:"))
m=int(input("2:"))
a=l[n]
b=l[m]
l[n]=b
l[m]=a
print(l)