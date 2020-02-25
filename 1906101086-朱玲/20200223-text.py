#1.
a=int(input("请输入一个整数:"))
b=[1,10,20,30,40,50]
c=1
if a in b:
    print(False)
else:
    for i in range(1,a+1):
        c=c*i
    print("此整数的阶乘为:%d"%(c))

#2.
P,R,T=map(int,input("请输入P，R，T，并用“，”隔开:").split(","))
a=(P*R*T)/100
print("给定P，R，T的单利为:%d"%(a))

#3.
list1=[14,25,98,75,23,1,4,56,59]
list1.sort()
print("列表中最大的数是:%d"%list1[-1])

#4.
list2=[14,25,98,75,23,1,4,56,59]
b=len(list2)
print("已知数组[14,25,98,75,23,1,4,56,59]")
n=int(input("需要求得数组前n个位数的平方，n="))
a=0
if n<b:
    for i in list2[0:n]:
        a=a+(i*i)
    print("需要求得的数组前n个位数的平方:%d"%(a))
else:
    print("False")

#5.
list3=[14,25,98,75,23,1,4,56,59]
print("交换前列表:{}".format(list3))
a,b=map(int(input("请输入需要的交换数据的位置索引，并用“，”隔开:".split(","))))
c=list3[a]
d=list3[b]
list3[a]=d
list3[b]=c
print("交换后列表:{}.format(list3)")