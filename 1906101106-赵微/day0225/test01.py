#集合_两种方法
A = {'a', 'b', 'c'}
B = set('abc')
print(A, B)


'''
集合的差（补）
print(A-B)
集合的并操作
print(A|B)
集合的交
print(A&B)
不同时包含
print(A^B)


集合的增删
两种添加元素的方式
A.add('')
B.update({1,3},[4,2],'e')
print(A)
print(B)
'''


'''
A.remove('a')
A.remove('b')
A.discard('b')
A.pop()
print(A)
'''


#字典
dic = {'name': '小李', 'age': 19, 'school': 'sctu'}
print(dic)

'''
修改数据
dic['name']='小四'
print(dic)

查找数据
dic.get('address')
dic.setdefault('address','成都')
print(dic)

增加数据
dic['class']='3班'
print(dic)

删除数据（键和值）
del dic['name']
print(dic)
dic.pop('age')#
print('dic')#
dic.popitem() #返回并随机删除最后一对键和值
print(dic)
'''

#条件判断
'''
age=int(input("please enter your age:"))
if age>=18:
    print("you are an adult")
else:
    print("you are not an adult")
'''


#==是等于，比较两个值是否相等
'''
num1=25
num2=1
while(num1!=num2):
    num2=int(input("输入你猜的数字："))
    if num1>num2:
        print("猜小了")
    elif num1<num2:
        print("猜大了")

print("猜对了")
'''

#if嵌套
'''
num=int(input("请输入一个数字："))
if num%2==0:
    if num %3==0:
        print("这个数字既能被2也能被3整除")
    else:
        print("这个数字能被2整除，不能被3整除")
    else:
        if num%3==0:
            print("这个数字可以被3整除，不能被2整除")
        else:
            print("既不能被3整除，也不能被2整除")
'''

#while循环
'''
sum = 0
a = 1
while(a <= 100):
    sum = sum + a
    a = a + 1
print(sum)


while(a == 1):
    print("无限循环中")  #ctrl+c结束循环


count = 0
while count < 5:
    print(count,"<5")
    count = count+1
else:
    print(count,"=5")

    
count = 0
while count < 5:
    print(str(count), "<5")
    count = count+1
else:
    print(str(count) + "=5")

#for循环遍历列表与字符串
'''


'''
list1=[1,2,3,4]
for i in list1:
    print(i)

str1='abcde'
for j in str1:
    print(j)
'''
'''
for i in range(0,11,3):
    print(i)
'''


'''
list1 = [1,2,3,2,6,10,1]
a = list1[0]
for i in list1:
    if i > a:
        a = i
print(a)
'''

'''
list2 = [1,2,3,4,'a',1,'b',21]
sum = 0
for i in list2:
    if isinstance(i,int):
        sum = sum + i
print(sum)
'''

'''
x = 5
for i in range(1,x):
    if x % i == 0:
        print("不是素数")
        break
    else:
        print("是素数")
'''


'''
x = 4
sum = 0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum = sum + 1
print(sum)
'''

#函数

def AplusB(a,b):
    return a+b

result=AplusB(1,2)
print(result)
print(AplusB(10,12))

#例1：传入半径r，计算圆面积
'''
def s(r):
    return 3.14*r*r
print(s(4))
'''
def s(r):
    area = r**2*3.14
    pi = 3.1415926
    return area,pi

area,pi = s(3)
print(pi,area)

'''
def s(r,pi):
    area = r**2*pi

    return area
print(s(5,3.1415926))
print(s(pi=3.1415926,r=6))
#调用方式
1.
s(6,3.14)
2.
s(pi=3.14,r=6)

'''


