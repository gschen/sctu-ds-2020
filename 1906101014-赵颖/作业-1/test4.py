n=int(input())
list=[14,25,98,75,23,1,4,56,59]
num=[]
lenth=len(list)
for i in range (n):
    num.append(list(i)**2)
T=sum(num)
print(T)