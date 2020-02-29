#1
x=int(input("输入要求阶乘的数:"))
s=1
if x not in [1,10,20,30,40,50]:
    for i in range(1,x+1):
      s=s*i
    print(s)
else:
    print("所输入数不符合要求")


#2
P=int(input('P='))
R=int(input('R='))
T=int(input('T='))
print('%d'% ((P*T*R)/100))


#3
list=[14,25,98,75,23,1,4,56,59]
list1=list
list1.sort()
print(list1[-1])

#4
list = [14,25,98,75,23,1,4,56,59]
n = int(input())
sum = 0
for i in range(0,n):
    a = list[i]**2
    sum += a
print(sum)

#5
l=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input().split())
if a>len(l) or b>len(l):
    print('超出范围')
l[a],l[b]=l[b],l[a]
print(l)