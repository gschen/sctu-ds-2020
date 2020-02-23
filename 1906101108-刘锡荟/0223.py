#1求给定数的阶乘
a=int(input('请输入一个整数:'))
b=[1,10,20,30,40,50]
c=1
if a in b:
    print(Flase)
else:
    for i in range(1,a+1) :
        c=c*i
        print('此整数的阶乘为：%d'%(d))   
#2单利
P,R,T=map(int,input("请依次输入P,R,T,并用", "隔开:").split(", "))  
a=(P*R*T)/100
print("所给定P,R,T的单利为:%d"%(a))      
#3查找数组中的最大元素
list=[14,25,98,75,23,1,4,56,59]
list.sort()
print('列表中最大的数是：%d'%list[-1])
#4求数组中的前n个数的平方和
list1=[14,25,98,75,23,1,4,56,59]
b=len(list1)
print('已知数组[14,25,98,75,23,1,4,56,59]')
n=int(input('需要求得的数组前n个位数的平方，n='))
a=0
if n<b:
    for i in list1[0:n]:
        a=a+(i*i)
        print('需要求得的数组前n个位数的平方为：%d'%(a))
else:
    print('Flase')
#5交换列表中的任意两个元素
list2=[14,25,98,75,23,1,4,56,59]
print('交换前列表：{}'.format(list2))
a,b=map(int,input("请输入需要交换的元素的位置索引，并用“,”隔开：").split(",")) 
c=list2[a]
d=list2[b]
list2[a]=d
list2[b]=c
print('交换后列表：{}'.format(list2))
