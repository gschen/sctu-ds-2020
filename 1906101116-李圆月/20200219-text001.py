a='hi'
b='s'
print(a+b)

c='hi'
print(c*3)

str='yahahuo'
print(str[0])
print(str[-1])
print(str[0:4])

#格式化输入
print('我叫%s'%('李圆月'))
print('现在已经是%.1f点啦'%9)

list=[1,2,3,[4,5,6]]
list1=[7,4,6,2,3,1]
list1.append(5)
list1.extend([1,2])
list1.pop(1)
list1.sort()
print(list1)
print(len(list))

tuple('haha',2,[1,2,3])
print(tuple)
#元组里面的元素不可修改


#day0219
#1
a=1
b=int(input('请输入一个数字：'))
c=[1,10,20,30,40,50]
if b in c:
    print(false)
else:
    for i in range(1,b+1):
        a=a*i
    print(a)
    
#2
P,R,T=map(int,input('请依次输入P R T,用,间隔').split(','))
x=(P*T*R)/100
print('单利:',x)

#3
list=[14,25,98,75,23,1,4,56,59]
list.sort()
print('最大的数是%s'%list[-1])

#4
a=0
list1=[14,25,98,75,23,1,4,56,59]
n=int(input('n='))
for i in list1[0:n]:
    a=a+(i*i)
print(a)

#5
list=[14,25,98,75,23,1,4,56,59]
x,y=map(int,input('请输入要交换元素的位置（第几个数）').split(','))
print('交换前',list )
z=list[x-1]
l=list[y-1]
list[y-1]=z
list[x-1]=l
print('交换后',list)
