#集合
#构建集合两种方法

A=('a','b','c','c',1)#然后每个元素用逗号隔开，字符串类型的数据需要加定界符。

B=set('aabbcce')#注意使用的是小逗号，所有元素放在一起。
#print(A,B)

#集合之间的运算
#集合之间的差(补)
#print(A-B)
#集合的并操作
print(A|B)
#集合的交
#print(A&B)
#不同的包含
#print(A^B)

#集合的增删
#添加元素的两种方法
A.add('d')
B.update((1,3),[4,2],'e')
print(A)
print(B)

#删除元素的三种方法

A.remove('a')
A.remove('f')
#A.discard('f')

#A.pop()
#print(A)


#字典

dic={'name':'张三','age':19,'school':'sctu'}

print(dic)
#修改数据
dic['neme']='李四'
print(dic)
#查找数据
#dic.get('address')
#dic.setdefault('name')
#dic.setdefault('address','成都')
#print(dic)
#增加数据
dic['class']='1班'
print(dic)


#删除数据
#del dic['name']

dic.pop('age')
print(dic)
#dic.popitem()
#print(dic)

age=int(input("请输入你的年龄"))

if age >= 18:
    print("你已经成年了")
else:
    print("你还为成年")

num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input("请输入你猜的数字："))
    if num1 > num2:
        print("你输入的值小了")
    elif num1 < num2:
        print("你输入的值大了")
    print("猜对了")

    num = int(input("请输入一个数字："))
    if num % 2 == 0:
        if num % 3 == 0:
            print("这个数字既能被2整除也能被3整除")
        else：
            print("这个数字能被2整除，不能被3整除")
    else:
        if num % 3 == 0:
            print("这个数字可以被3整除，不能被2整除")
        else:
            print("既不能被3整除，也不能被2整除")
        
sum = 0
a = 1
while(a <= 100):
    sum = sum + a
    a = a + 1
print(sum)

while():
    print("无限循环！！！")

count = 0

while count < 5:
    print(str(count),"<5")
    count = count + 1
else:
    print(str(count)+"=5")

list1 = [1,2,3,4,5]
for i in list1:
    print(i)

for i in range(5):
    print(i)
for i in range(0,11,3):
    print(i)

print(list(range(5)))

list1 = [1,2,3,2,6,10,1]

a = list1[0]

for i in list1:
    if i > a:
        a = i
print(a)

list2 = [1,2,3,'a',1]

sum = 0

for i in list2:
    if isinstance(i,int):
        sum = sum + i
print(sum)


x = 6
for i in range(2,x):
    if x % i == 0:
        print("不是素数")
        break
else:
    print("是素数")

x = 5
sum = 0

for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum = sum + 1
print(sum)

def banjin(r):
    s=3.14*r**2
    return s
print(banjin(5))

s=lambda r,pi:r**2*pi
print(s(3,3.14))

def  change(a):
    a=10

b=2
change(b)
print(b) #不可改


c=[1,2,3]
def change(x):
    x.append([1,2,3])
change(c)
print(c)  #可改


b='123'
b=123

def Main(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])

Main(1,11,12,13,143)

