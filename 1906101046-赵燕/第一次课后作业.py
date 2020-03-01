#求给定数的阶层
a=int(input('please enter:'))
b=1
if a == 0:
    print('0的阶乘为1')
if a < 0:
    print('负数没有阶乘')
else:
    for i in range(1,a+1):
        b=b*i
print('%d的阶乘是%d'%(a,b))



#单利公式
p,t,r=map(int,input().split())
print(int(p*t*r/100))


#查找组数中最大元素
list1=[14,25,98,75,23,1,4,56,59]
print(max(list1))


#求数组中的前n个数的平方和
list1=[14,25,98,75,23,1,4,56,59]
n=int(input())
s=0
if n<len(list1):
    while n>0:
        s=s+list1[n-1]**2
        n-=1
print(s)



#交换列表里的任意元素
listl=[14,25,98,75,23,1,4,56,59]    
a=int(input('请输入要替换的位置：'))
b=int(input('请输入要替换的位置：'))
listl[a],listl[b]=listl[b],listl[a]
print(listl)


