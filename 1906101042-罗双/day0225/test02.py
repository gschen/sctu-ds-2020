#集合
#构建集合两种方法

A={'a','b','c','c',1}#然后每个元素用逗号隔开，字符串类型的数据需要加界定符
B=set('aabbcce')#注意使用的是小括号，所有元素放在一起
print(A,B)

#集合之间的运算
#集合之间的差（补）
print(B-A)
#集合的并操作
print(A|B)
#集合的交
print(A&B)
#不同时包含
print(A^B)

#集合的增删
#添加元素的两种方法
A.add('d')#为集合添加元素，当元素存在时则不操作
B.update({1,3},[4,2],'e')#给集合添加元素，参数可以是列表，元组，字典等
print(A)
print(B)

#删除元素的三种方法
A.remove('a')
A.remove('f')#移除指定元素，元素不存在则会发生错误
A.discard('f')#移除指定元素，元素不存在不会发生错误

x=A.pop()#随机移除元素
print(x)


#字典
#格式：d={key1:value1,key2:value2}
#特点：键必须唯一，值可以多样
dic={'name':'张三','age':19,'school':'sctu'}

#修改数据
dic['name']='李四'
print(dic)
#查找数据据
dic.get('address')
dic.setdefault('name')
dic.setdefault('address','成都')#dic.setdefault(key,default=None)如果键不存在于字典中，将会添加键并将值设为default
print(dic)
#增加数据
dic['class']='1班'
print(dic)

#删除数据
del dic['name']
print(dic)
dic.pop('name')#key值必须给出
dic.popitem()#随机返回并删除字典中的最后一对键和值
print(dic)




#条件判断和循环
#例子1
age=int(input("请输入你的年龄："))
if age >= 18:
    print("你已经成年了")
else:
    print("你还未成年")

#例子2
num1=25
num2=1
while(num1 != num2):
    num2=int(input("请输入你猜的数字："))
    if num1 > num2:
        print("你输入的值小了")
    elif num1 < num2:
        print("你输入的值大了")
print("猜对了")

#例子3
num=int(input("请输入一个数字："))
if num % 2 ==0:
    if num % 3 ==0:
        print("这个数能被2和3整除")
    else:
        print("这个数能被2整除，不能被3整除")
else:
    if num % 3==0:
        print("这个数能被3整除，不能被2整除")
    else:
        print("这个数既不能被3整除，也不能被2整除")

#while循环
sum=0
a=1
while(a <= 100):
    sum = sum + a
    a=a+1
print(sum)
#无限循环
while(True):
    print("无限循环中！")#ctrl+c 停止

#例子4
count=0
while count < 5:
    print(count,"<5")
    count=count+1
else:
    print(str(count)+"=5")

#for 循环遍历
list1=[1,2,3,4,5]
for i in list1:
    print(i)

str1 ='abcdefg'
for j in str1:
    print(j)

for i in range(5):
    print(i)

for i in range(2,100):
    print(i)

for i in range(0,11,2):
    print(i)  #此处2为步长

print(list(range(5)))

#给定一个列表，找出列表中最大的元素
list1=[1,2,3,2,6,10,1]
a=list1[0]
for i in list1 :
    if i>a:
        a=i
print(a)

#计算列表中数字之和
list2=[1,2,3,4,'a',1,'b',21]
sum=0
for i in list2:
    if isinstance(i,int):
        sum=sum+i
print(sum)    


#for 判断素数
x=5
for i in range(2,x):
    if x % i ==0:
        print("不是素数")
        break
else:
    print("是素数")

#输入x，检查2-x之间有多少个素数
x=10
sum=0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        sum=sum+1
print(sum)



#函数

def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)
print(AplusB(1,2))

#传入半径R，计算圆的面积
def circle(r):
    return r**2*3.14
print(circle(5))

# #错误示例
# a=2 #全局变量(局部空间内可访问)
# def main():
#     b=3 #局部变量（全局空间内不可访问）
#     print(a)
# main()
# print(b)#结果报错


#匿名函数：lambda
#lambda函数：def的单行形式
circle2=lambda r,pi:r**2*pi
print(circle2(3,3.14))

#传入不可更改对象(字符串，元组，数字)实例
def change(a):
    a=10
b=2
change(b)#b=a=10
print(b)#结果是2

#传入可更改对象
#可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print("函数内取值：",mylist)
    return
#调用changeme函数
mylist=[10,20,30]
changeme(mylist)
print("函数外取值：",mylist)


#关键字参数
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


#不定长函数
def main(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])
main(1,11,12,13,14)