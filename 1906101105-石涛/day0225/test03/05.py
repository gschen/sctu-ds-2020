# coding=utf-8

# no.1
list1=[1,1,3,2,10,6]
a=list1[0]
for i in list1:
    if i>a:
        a=i
print(a)

# no.2
list2=[1,2,3,4,'a',1,'b','c']
sum=0
for i in list2:
    if isinstance(i,int):
        sum+=i
print(sum)

# no.3
x=5
for i in range(2,x):
    if x%i==0:
        print('不是素数')
        break
else:
    print('是素数')

# 素数个数计算
x=10
sum1=0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        sum1+=1
print(sum1)