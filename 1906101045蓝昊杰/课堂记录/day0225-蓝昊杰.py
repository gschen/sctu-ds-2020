#构建集合两种方法
A={'a','b','c','c',1}#然后每个元素用逗号隔开，宁符串类型的数据需要加定界符
B=set('aabbcce')#注意使用的是小括号，所有元索放在一起。
print(A,B) 
#集合之间的运算
#集合的差(补) 
print(A-B)
#集合的并操作
print(A|B)
#集合的交
print(A&B)
#不同时包含
print(A^B)
#集合的增删
#添加元素的两种方法
A.add('a')
B.update({1,3},[4,2],'e')
print(A)
print(B)
#删除元素的三种方法
A.remove('a') 
A.discard('f')
x=A.pop()
print(x)
#字典
dic={'name':'张三','age'  :19, 'school':'sctu'}
#修改数据
dic['name']= '李四'
#查找数据
dic.get('address')
dic.setdefault('name')
dic.setdefault('address','成都' )
#增加数据
dic['class']='1班'
#删除数据
del dic['name']
dic.pop('age')
dic.popitem()#删除最后一个，然后返回值








#判断和循环语句
age = int(input("请输入你的年龄"))
if age>=18:
    print("你已经成年啦" )
else:
    print("你还未成年")




# numl = 25
# num2 = 1
# while(num1!=num2):
#     num2 = int(input("请输入你猜的数字:"))
#     if numl>=num2 :
#         print("你输入的值小了")
#     elif num1<num2:
#         print("你输入的值大了")
# print("猜对了")




# num = int(input("请输入个数子:")
# if num%2==0:
#     if num%3==0:
#         print("这个数子既能被2也能被3整除")
#     else:
#         print("这个数字能被2整除不能放3整除")
# else:
#     if num%3==0:
#         print("这个数字可以被3整除，不能被2整除")
#     else:
#         print("既不能被2整除，也不能被3整除”)



# sum=0
# a=1
# while a<=100:
#     sum=sum+a
#     a=a+1
# print(sum)



# while count < 5:
#     print(str(count),"<5")
#     count = count + 1
# else:
#     print(str(count)+"=5")



# list1 = [1,2,3,4,5] 
# for i in list1:
#     print(i)
# str1 ='abcdefg'
# for i in str1:
#     print(j)
# for i in range(5):
#     print(i)
# for i in range(2,10):
#     print(i)
# for i in range(0,11,3):
#     print(i) 
# print(list(range(5)))


#练习题
#给定一个列表，找列表中最大的元素
list1 = [1,2,3,2,6,10,1]
a = list1[0]
for i in list1:
    if i>a:
        a=i
print(a)


#计算列表中数字之和
list2 = [1,2,3,4,'a',1,'b',21]
sum=0
for i in list2:
    if isinstance(i,int):
        sum=sum+i
print (sum)


#输入n，检查2到n之间有多少素数
x=6
for i in range(2,x): 
    if x%i==0:
        print("不是素數")
        break
else:
    print("是素数")



x=5
sum=6
for i in range(2,x+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum=sum+1
print(sum)



#函数
#计算圆面积
def js(r):
    return 3.14*r**2



#形参和实参

#形参
def area(r):
    s = r**2*3.14
    return s

#实参
def area(r=6):
    s = r**2*3.14
    return s

# # def abc(r,pi):
#     s = r**2*pi
#     return s
# print(abc(6,3.14))
# print(abc(r=6,pi=3.14))


#lambda函数
circle = lambda r,pi:r**2*pi
print(circle(3,3.14))


#python传不可变对象实例
def chage(a):
    a = 10
# b = 2#此时传入的是2不是b，a=2,然后a又被赋值为10.b依然为2
# chage(b)#相当于b=a
# print(b)

#python传入可更改对象
c=[1,2,3]
def chage2(x):
    x.append([1,2,3])
chage2(c)
print(c)


#不定长参数
def printinfo(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])
printinfo(1,11,12,13,14,15)