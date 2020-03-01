#集合
#构建集合两种方法

A={'a','b','c','c',1}#然后每个元素用逗号隔开，字符串类型的数据需要加定界符。

B=set('aabbcce')#注意使用的是小括号，所有元素放在一起。
#print(A,B)

#集合之间的运算

#集合的差（补）
#print(A-B)
#集合的并操作
#print(A|B)
#集合的交
#print(A&B)
#不同时包含
#print(A^B)

#集合的增删

#添加元素的两种方法
#A.add('a')
#B.update({1,3},[4,2],'e')
#print(A)
#print(B)
#删除元素的三种方法
#A.remove('a')
#A.remove('f')
#A.discard('f')
#A.pop()
#print(A)

#字典
#dic={'name':'张三，'age':19,'school':'sctu'}
#修改数据
#dic['name']='李四'
#print(dic)
#查找数据
#dic.get('address')
#dic.setdefault('sddress','成都')
#print(dic)
#增加数据
#dic['class']='1班'
#print(dic)
#删除数据
#del dic['name']
#dic.pop('age')
#print(dic)
#dic.popitem()
#print(dic)

#1
age = int(input('请输入你的年龄'))

if age >= 18:
    print('你已经成年啦')
else:
    print('你还未成年')

#2
num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input('请输入你猜的数字：'))
    if num1 > num2:
        print('你输入的值小了')
    elif num1 < num2:
        print('你输入的值大了')
print('猜对了') 

#3
num = int(input('请输入一个数字：'))
if num % 2 ==0:
    if num % 3 ==0:
        print('这个数字既能被2也能被3整除')
    else:
        print('这个数字能被2整除，不能被3整除')
else:
    if num % 3 ==0:
        print('这个数字能被3整除，不能被2整除')
    else:
        print('既不能被3整除，也不能被2整除')

#4
sum = 0
a = 1
while(a <= 100):
    sum = sum + a
    a = a + 1
print(sum)

#5
while(a == 1):
    print('无限循环中！！！')

#6
count = 0
while count < 5:
    print(count,'<5')
    count = count + 1
else:
    print(count,'=5')                                    

#7
list1 = [1,2,3,4,5]
for i in list1:
    print(i)

str1='abcdefg'
for j in str1:
    print(j)

for i in range(5):
    print(i)

for i in range(2,10):
    print(i)

for i in range(0,11,2):
    print(i)    

#8
print(list(range(5)))

#9
list1 = [1,2,3,2,6,10,1]
a = list1[0]
for i in list1:
    if i > a:
        a = i
print(a)     

#10
list2 = [1,2,3,4,'a',1,'b',21]
sum = 0
for i in list2:
    if isinstance(i,int):
        sum = sum + i
print(sum) 

#11
x = 6
for i in range(2,x):
    if x % i == 0:
        print('不是素数')
    else:
        print('是素数')

#12
x = 5
sum = 0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum = sum + 1
print(sum)

#13
def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)
print(AplusB(10,12))

def circle(r):
    area=r**2*3.14
    pi=3.1415926
    return area,pi

area,pi=circle(5) 
print(pi.area)

def circle(r,pi):
    area=r**2*pi
    return area

circle3=lambda r,pi:r**2*pi
print(circle3(3,3.14))   

#14
c=[1,2,3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)    



