'''集合  1.构建集合的两种方法'''
A={'a','b','c','c',1}
B=set('aabbcce')#小括号，所有集合放在一起。
print(A,B)

'''2.集合之间的运算'''
print(A-B)#集合的差（补）
print(A|B)#集合的并
print(A&B)#集合的交
print(A^B)#不同时包含

'''3.集合的增删'''
#添加元素的两种方法
A.add('d')
B.update({1,3},{4,2},'e')
print(A)
print(B)

#删除元素的三种方法
A.remove('a')
A.discard('f')
x=A.pop()
print(x)

'''字典'''
dic={'name':'李子维','age':37,'school':'风南'}
print(dic)

#修改数据
dic['name']='王诠胜'

#查找数据(setdefault() 函数和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。)
dic.get('name')
dic.setdefault('address',default='台北')
print(dic)

#增加数据
dic['class']='1班'
print(dic)

#删除数据
def dic['name']
dic.pop('name')
dic.popitem()
print(dic)

'''条件结构与循环小练习'''
#小练习1
lis=[1,2,3,2]
 a = lis[0]
for i in list1:
    if i > a:
        a=i
print(a)

#小练习2
lis = [1,2,3,'a']
sum = 0
for i in lis:
    if isinstance(i,int):
        sum = sum + i
print(sum)

#小练习3
x = 5
sum = 0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum = sum + 1
print(sum)

'''函数'''
#定义
#函数语法
'''
def 用户自定义函数名（参数1，参数2）：
        代码块
        return 返回结果
'''
def asd(a,b):
    c=a+b
    return c

def asd(a,b):
    return a+b

#实例与调用例题
def circle(r):
    area=r**2*3.14
    return area
print(circle(5))

#参数传递
def circle(r):#形参
def circle(r=10):#实参

#参数传递
#def 函数名（形参1，形参2...实参1，实参2）
circle(r,pi)
circle(6,3.14)
ciecle(pi=3.14,r=6)

#命名空间
'''
局部空间内可访问全局空间
全局空间内不可访问局部空间
'''

#匿名函数：lambda
#变量名=lambde参数1，参数2...：返回结果
circle=lambde r,pi:r**2*pi

#传可更改对象和不可更改对象
'''
定义: string,tuples和numbers不可更改对象
      list,dict可以修改对象













