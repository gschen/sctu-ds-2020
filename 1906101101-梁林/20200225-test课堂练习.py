#集合构建
A={'f','h',6}
B=set('dfggd')
print(A,B)
#并，交，补集
print(A|B)
print(A&B)
print(B-A)
print(A^B)
#集合增加删除
A.add('j')
A.add('h')
print(A)
B.update([1,2,3],'llo')
print(B)

A.remove('h')#遇见不存在元素报错
A.discard('y')#不会报错
print(A)
A.pop()#随机删除
print(A)

#字典
dic={'A':1,'B':2,'C':3}
print(dic)
#修改数据
dic['A']=6
print(dic)
#查找数据
print(dic.get('A'))
print(dic.get('D'))
print(dic.setdefault('D',4))#字典不存在自动创建，并赋值
print(dic)
#删除数据
del dic['A']
print(dic)
print(dic.pop('B'))
print(dic)

print(dic.popitem())#
print(dic)


#if
age=int(input('请输入年龄：'))
if age>=18:
    print('成年')
else:
    print('未成年')
#猜数字游戏
N=7#初始值
s=1
n=5
while n!=N:
    n=int(input('请输入一个数字：'))
    if n>N:
        print('值大了')
        s+=1
    elif n<N:
        print('值小了')
        s+=1
print('猜对了，用了%s次'%s)

#if嵌套
f=int(input('请输入一个数字：'))
if f%2==0:
    if f%3==0:
        print('该数能被2与3整除')
    else:
        print('该数能被2整除，但不能被3整除')
else:
    if f%3==0:
        print('该数能被3整除，但不能被2整除')
    else:
        print('该数不能被2与3整除')

#循环
#求1到100的和
a=0
x=0
while a<100:
    a+=1
    x+=a
print(x)

#无限循环
while True:
    print(1)

#else while 
g=2
while g<7:
    print('g<',7)
    g+=1
else:
    print('g=',g)

#for循环
list=[1,2,3,4,5]
for i in list:
    print(i)
#range
for i in range(7):
    print(i)
for i in range(5,7):
    print(i)
for i in range(1,10,2):
    print(i)
print(list(range(5)))

#找最大数
a=[1,2,3,4,5,6,9,8]
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        a[i+1]=a[i]
print(a[-1])
#求和
a=[1,2,3,4,'f','j',9]
s=0
for i in a:
    if type(i)==int:
        s+=i
print(s)

#找质数
n=10
m=0
for i in range(2,n+1):
    for ii in range(2,i):
        if i%ii==0:
            break
    else:
        m+=1
print(m)



#圆的面积
def mj(x):
    return x**2*3.14
print(mj(2))

#固定参数
def mj(x=5):
    pass
#
a=2
def mj():
    b=3
    print(a)
mj()
print(a,b)

#lambda
a=lambda x:x**2
print(a(8))

#不可更改对象
def mj(a):#传入的是b的值2
    a=10
b=2
mj(b)
print(b)

#可更改对象
c=[1,2,3]
def change2(x):#传入的本身
    x.append([1,2,3])
change2(c)
print(c)

#
def main(x,*y):
    print(x)
    print(y)
print(main(1,51,5,1,8,1))


