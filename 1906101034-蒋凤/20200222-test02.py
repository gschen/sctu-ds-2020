1.
num=8
s = 1
for i in range(1,num+1):
    s*=i
print('%d的阶乘是：%d'%(num,s))

2.
P=int(input('本金P = '))
T=int(input('时间T = '))
R=int(input('利率R = '))
S=(P*T*R)/100
print('单利是%d'%(S))

3.
list=[14,25,98,75,23,1,4,56,59]
print(max(list))

4.
List=[14,25,98,75,23,1,4,56,59]
p=len(List)
print('列表的长度是 %d'%len(List))
n=int(input('请输入一个0到9的整数：'))
if 0 <n <= p:
    sum=0
    for m in List[:n]:
        sum=sum+m*m
    print(sum)
else:
    print('False')
    print('请重新输入一个0—9的数字！')


5.
n=int(input('请输入一个数：'))
m=int(input('请输入一个数：'))
test=[14,25,98,75,23,1,4,56,59]
temp=test[n]
test[n]=test[m]
test[m]=temp
print(test)

