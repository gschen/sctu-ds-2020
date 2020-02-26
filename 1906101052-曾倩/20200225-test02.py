A={'a','b','c','d,1'}
B=set('aabbccdd')
#集合的差(补)
#print(A-B)
#集合的并
#print(A|B)
#集合的交
#print(A&B)
#不同时包含
#print(A^B)

#集合的增减
#A.add('b')
B.update({1,3},[4,2],'e')
#print(A)
#print(B)

#删除元素

# A.remove('a')
# A.remove('f')
# A.discard('f')

# A.pop('a')
# A.pop()
# print(A)

dic={'name':'张三','age':19,'school':'sctu'}
print(dic)
#修改数据
#dic['name']='李四'

#查找数据
dic.get('address')
dic.setdefault('name')
dic.setdefault('address','成都')
print(dic)
#增加数据
dic['class']='二班'


age = int(input("请输入年龄"))
if age >= 18:
    print("你已经成年了")
else:
    print("你还未成年")

# num1=25
# num2=1
# while (num1 !=num2):
#     num2 = int(input("请输入你猜的数字"))
#     if num1 > num2:
#         print('你输入的值太小了')
#     elif num1 < num2:
#         print('你输入的值太大了')
#     else:
#         print('猜对了')


num = int(input("亲输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("这个数字既能被二整除，也能被三整除")
    else:
        print("能被二整除，不能被三整除")
else:
    if num % 3 == 0:
        print("这个数字可以被三整除，不能被二整除")
    else:
        print("既不能被3整除，也不能被2整除")


sum = 0
a = 1
while (a <= 100):
    sum = sum + a
    a=a+1
print(sum)

while (a == 1):
    print("无限循环中！！！")

count = 0
while count < 5:
    print(str(count),"<5")
    count = count + 1
else:
    print(str(count)+"-5")

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

for i in range(0,11,3):
    print(i)

print(list(range(5)))

list1=[1,2,3,2]
a=list1[0]
for i in list1:
    if i > a:
        a=i
print(a)

print(isinstance(1,int))

list2=[1,2,3,4,'a',1]
sum=0
for i in list2:
    if isinstance(i,int):
        sum=sum+1
print(sum)

x=5
for i in range(2,x):
    if x % i == 0:
        print("不是素数")
        break
else:
    print("是素数")

x = 10
sum = 0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum = sum + 1
print(sum)

#3
def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)
print(AplusB(10,12))

def circle(r):
    area=r**2*3.14
print(circle(2))


# def abc(r,pi):
#     s = r**2*pi
#     return s
# print(abc(6,3.14))
# print(abc(r=6,pi=3.14))


#lambda函数
# circle = lambda r,pi:r**2*pi
# print(circle(3,3.14))


def ChangeInt(a):
    a=10
b=2
ChangeInt(b)
print(b)

#可改
c=[1,2,3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)

def main(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])

# def printinfo(x,*y):
#     print(x)
#     for i in range(len(y)):
#         print(y[i])
#printinfo(1,11,12,13,14,15)
