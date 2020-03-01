#第一周python培训
A={'a','b','c','c','f',1}
B=set('aabbcc')
#print(A,B)

#集合之间的运算
#集合的差（补）
#print(A-B)
#集合的并操作
#print(A|B)
#集合的交操作
#print(A&B)
#不同时包含
#print(A^B)

#集合的增删
#添加集合的两种方法
#A.add('e')
#print(A)
#B.update({1,3},{2,4},'e')
#print(B)

#删除元素的三种办法
#A.remove('a')
#A.remove('f')
#A.discard('f')
#A.pop()
#print(A)

#字典
dic={'name':'张三','age':19,'school':'sctu'}
#print(dic)
#修改数据
#dic['name']='李四'
#print(dic)

#查找数据
#dic.get('address')
#dic.setdefault('name')
#dic.setdefault('address','成都')
#print(dic)

#增加数据
#dic.['class']='3班'
#print(dic)

#删除数据
#del dic['name']
#print(dic)
#dic.pop('age')
#print(dic)
#dic.popitem()
#print(dic)



#条件判断
'''
age=int(input('请输入你的年龄'))
if age >=18:
    print('成年')
else:
    print('未成年')
'''
'''
num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input('请输入你猜的数字:'))
    if num1>num2:
        print('你输入的值小了')
    elif num1<num2:
        print('你输入的值大了')
print('猜对了')
'''
'''
num = int(input('请输入一个数:'))
if num % 2 == 0:
    if num % 3 == 0:
        print('这个数既能被2整除也能被3整除')
    else:
        print('这个数能被2整除，不能被3整除')
else:    
    if num %3 == 0:
        print('这个数字能被3整除，不能被2整除')
    else:
        print('既不能被3整除，也不能被2整除')
'''
'''
sum = 0
a = 1
while(a<=100):
    sum=sum+a
    a=a+1
print(sum)        
'''
'''
count=0
while count < 5:
    print(str(count),"<5")
    count = count + 1
else:
    print(str(count)+"=5")    
'''
'''
#for循环
list1 = [1,2,3,4,5]
for i in list1:
    print(i)
'''
'''
str1 = 'asdfghjkl'
for i in str1:
    print(i)
'''
'''
for i in range(2,10):
   print(i)
for i in range(0,11,2):
   print(i)
'''
'''
print(list(range(5)))
'''

#练习题
#给定一个列表，找列表中最大的元素
'''
list=[1,2,3,4,7,5,8,6,10]
a=list[0]
for i in list:
    if i > a:
        a = i
print(a)        
'''
#计算列表中数字之和
'''
list=[1,2,3,4,'a',1]
sum=0
for i in list:
    if isinstance(i,int):
        sum=sum+i
print(sum)        
'''
#输入n，检查2到n之间有多少素数
'''
x=int(input())
for i in range(2,x):
    if x % i == 0:
        print('不是素数')
        break
else:
    print('是素数')    
'''
'''
x=5
sum=0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum=sum+1
print(sum)        
'''

#函数
'''
def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)
print(AplusB(10,12)) 
'''   
#求圆的面积
'''
import math
def area(r):
    return math. pi*r*r
result=area(3)
print(result)
'''
#def f(r):
  #  return r**2*3.14
#print(f(5))   
''' 
def circle(r,pi):
    area=r**2*pi
    return area
print(circle(6,3.14))    
''' 
#形参
'''
def area(r):
    s = r**2*3.14
    return s
'''
#实参
'''
def area(r=6):
    s = r**2*3.14
    return s

def abc(r,pi):
    s = r**2*pi
    return s
print(abc(6,3.14))
print(abc(r=6,pi=3.14))
'''
#匿名函数:lambda
'''
circle=lambda r,pi:r**2*pi
print(circle(2,3.14))
'''
#python传不可变对象实例
'''
def chage(a):
    a = 10
b = 2#此时传入的是2不是b，a=2,然后a又被赋值为10.b依然为2
chage(b)#相当于b=a
print(b)
'''
#python传入可更改对象
'''
c=[1,2,3]
def chage2(x):
    x.append([1,2,3])
chage2(c)
print(c)
'''
#不定长参数
'''
def printinfo(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])
printinfo(1,11,12,13,14,15)
'''