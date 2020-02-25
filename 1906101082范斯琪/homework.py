#1
a=int(input('输入一个整数：'))
b=[1,10,20,30,40,50]
c=1
if a in b:
    print('False')
else:
    for i in range(1,a+1):
        c=c*i    
    print('此整数阶乘：%d'%(c))  

#2
P*T*R=map(int,input().split())
a=P*R*T/100   
print('单利为:%d'%(a))  

#3
a=[14,25,98,75,23,1,4,56,59]
a.sort()
print('最大的数是：%d'%a[-1])

#4
lis1=[14,25,98,75,23,1,4,56,59]
b=len(lis1)
print('已知数组[14,25,98,75,23,1,4,56,59]')
n=int(input('n='))
a=0
if n<b:
    for i in list1[0:n]:
        a=a+(i*i)
    print('求数组前n个位数的平方为：%d'%(a))
else:
    print('Flase')

#5
lis1=[14,25,98,75,23,1,4,56,59]
print("交换前列表：".format(list2))
a,b=map(int,input("请输入需要交换的元素的位置索引，并用','隔开：").split(","))
c=lis1[a]
d=lis1[b]
lis1[a]=d
lis1[b]=c
print("交换后列表：".format(lis1))