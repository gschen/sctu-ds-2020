A={'a','b','c','d',1}
B=set('abcde')
print(A|B)#交集
print(A-B)#补集
print(A^B)#并集

A.add('f')
B.update(1,'e',('gh'),{'kj'},['ui'])
print(A)
print(B)

A.remove('a')
A.discord('b')
print(A)

A.pop()#pop随机删除一个元素
print(A)
#
dic={'name':'岳彬睿','age':'19','home':'miangyang'}
dic['name']='Bruce'#修改
dic.get('age')#查找
dic['class']='2班'#增加
del dic['home']#删除
dic.pop('name')#删除
print(dic)
#
age=int(input('请输入你的年龄：'))
if age <18:
    print('未成年')
else:
    print('成年了')
#
num1=25
num2=1
while(num1 != num2):
    num2=int(input('请输入你猜的数：'))
    if num1>num2:
        print('太小了')
    elif num1<num2:
        print('太大了')
print('猜对了')
#
num=int(input('请输入一个数：'))
if num%2==0:
    if num%3==0:
        print('这个数既能被二整除又能被三整除')
    elif:
        print('这个数能被二整除不能被三整除')
else:
    if num%3==0:
        print('这个数可以被三整除不能被二整除')
    elif:
        print('这个数既不能被三整除也不能被二整除')
#
sum=0
a=1
while(a<=100):
    sum=sum+a
    a=a+1
print(sum)
#
while(num=100):
    print('错误！')
#
list=[1,2,3,4,5,6]
for i in list:
    print(i)
#
list=[1,3,4,'a',5,'b']
sum=0
for i in list:
    if isinstance(i,int):
        sum= sum+i
print(sum)
#
x=6
for i in range(1,x):
    if x%i==0:
        print('不是素数')
        break
    else:
        print('是素数')
#
x=5
sum=0
for i in range(2,x+1):
    for j inrange(2,i):
        if i % j==0:
            break
        else:
            sum=sum+1
print(sum)
#
def httc(a,b):
    return a+b
result=httc(1,2)
print(result)
print(httc(10,12))
#
def circle(r):
    area=r**2*3.14
    pi=3.1415926
    return area,pi
area,pi=circle(r)
print(area,pi)
#
def circle(r,pi):
    return r**2*pi
circle3=lambda r,pi:r**2*pi
print(circle3(3,3.14))
#
def change(a):
    a=10
#
b=2
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)
#
def main(x,*y):
    print(x)
#    print(y)
    for i in range(len(y)):
        print()
