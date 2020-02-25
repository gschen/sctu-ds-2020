#集合
#构建集合两种方法(无序的)
A={'a','b','c','c',1}
B=set('aabbcc')
print(A,B)

#集合之间的运算（交，并，补）
#集合的差（补）
#print（A-B）（把前面的作为他的全集）
#集合的并
#print(A|B)
#集合的交
#print(A&B)
#不同时的包含【A中有B中没有】
#print(A^B)

#集合的增加删除
#增添的两种方法
A.add('d')
B.update({1,3},[4,2],'e')#(对于集合字典字符串都可以)
print(B)
#删除的三种方法
A.remove('a')#如果没有元素会报错
A.discard('f')#删除没有的不会报错
A.pop()#随机删除一个数



#字典
#特点：键必须唯一，值可以多样
dic={'name':'张三'，'age':18,'school':'成都。。'}
print(dic)
#修改数据
dic['name']='李四'
#查找数据
#dic.get('name')
#dic.setdefault('address',default='成都')#（如果不存在这个键，就新加一个，存在就不返回）
#print(dic)
#增加数据
dic['class']='1班'
#删除数据
#del dic['name']#(同时删除对应的值)
#dic,pop('age')#(同时返回并删除对应的值)
#dic.popitem()#（返回并删除最后的键和值）
#print(dic)



age = int(input('请输入你的年龄'))
if age >= 18:
    print('你已经成年了')
else:
    print('你还未成年')


num1 = 25
num2 = 1
while(num1 !=num2):
    num2 = int(input('请输入你猜的数字：'))
    if num1 > num2:
        print('你输入的值小了')
    elif num1 < num2:
        print('你输入的值大了')
    else:
        print('猜对了')


num = int(input("请输入一个数字："))
if num % 2 == 0:
    if num % 3 ==0:
        print("这个数字既能被2整除又能被3整除")
    else:
        print("这个数字能被2整除，不能被3整除")
else:
    if num % 3 == 0:
        print("这个数字可以被3整除，不可以被2整除")
    else:
        print("既不能被3整除，也不能被2整除")


sum = 0
a = 1
while(a <= 100):
    sum = sum + a
    a = a + 1
print(sum)


while():
    print("无限循环中")


count = 0
while count < 5:
    print(str(count),"<5")
    count = count + 1
else:
    print(str(count)+"=5")



str1='abcdefg'
for j in str1:
    print(j)

for i in range(5):
    print(i)

for i in range(2,10):
    print(i)

for i in range(0,11,3):
    print(i)

list1=[1,2,3,4,10,6]
a=list1[0]
for i in list1:
    if i>a:
        a=i
print(a)


list2=[1,2,3,4,'a',1]
sum=0
for i in list2:
    if isinstance(i,int):
        sum=sum+i
print(sum)


x=5
for i in range(2,x):
    if x%i==0:
        print('不是素数')
        break
else:
    print('是素数')


x=10
sum=0
for i in range(2,x+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum=sum+1
print(sum)


def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)
print(AplusB(10,12))


def circle(r):
    return r**2*3.14
print(circle(5))


a=2#全局变量
def main():
    b=3#局部变量，局部空间可以访问全局变量，全局变量不可以访问局部变量，不可以直接调用
    print(a)#a=2
main()
print(b)#b没有定义


circle3=lambda r,pi:r**2*pi
print(circle3(3,3.14))


def change(a):
    a=10
b=2
change(b)
print(b)


c=[1,2,3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)


def main(x,*y):
    print(x)
    for i in y:
        print(y)
main(1,11,12,13,14)

