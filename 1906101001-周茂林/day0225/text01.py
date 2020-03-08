#集合构建方法
#1    
A = {'a', 's', 'd', 'f', 2}  
#2   
B = set('asdff1')
print(A, B)

#并
(A|B)
#交
（A&B）
#补集
（A-B）求b的补集，在b不存在
#不同是包含
（A^B）
#集合的增加    
 A.add('d')
#添加      
B.update({1, 3}, {4, 2}, 'e')
#删除    
A.remove('a')
A.discard('a')


#字典
dic={'name':'张三'，'school':'sctu', 'age':19}
#print(dic)
#修改
dic['name']='李四'
dic.get('adress')
#增加
dic.setdefault('adress', default='成都')
#or      dic['class']='1班'


#删除
del dic['name']
dic.pop('name')
dic.popitem()      #删除最后一个值


#条件判断
age=int(input('请输入你的年龄'))
if age >= 18:
    print('已成年')
else：
    print('未成年')

num1 = 25
num2 = 1
while num1 != num2:
    num2 = int(input('请输入你猜的数字'))
    if num1 > num2:
        print('你输入的值小了')
    elif num1 < num2:
        print('你输入的值大了')
    else:
        print('你猜对了')



num = int(input('请输入一个数字'))
if num % 2 == 0:
    if num % 3 == 0:
        print('这个数既能被2整除也能被3整除')
    else:('这个数能被2整除，不能被3 整除')
else：
if num % 3 == 0:
    print('这个数能被3整除')
else:
    print('既能被2整除，也能被3整除')


#   循环
sum = 0
a = 1
while a <= 100:
    sum += a+1
print(sum)


#无线循环
while a == 1:
    print('无限循环')



count = 0

while count < 5；
    print(str(count), '<5')
    count += 1
else:
    print(str(count) + '=5')



list1 = [1, 2, 3, 4, 5]
for i in list1:
    print(i)


srr1 = 'abcdefg'
for j in srr1:
    print(j)


for i in range(5):
    print(i)

#指定区间
for i in range(2, 10):
    print(i)

#创建列表
print(list(range(5)))


#练习题
#1
list1 = [1, 2, 3, 2]
a = list1[0]
  for i in list1:
      if i > a:
          a = i
print(a) 

#2
list2 = [1, 2, 3, 'a', 1]
sum = 0
for i in list2:
    if isinstance(i, int):
        sum += i
        print(sum)
#print(isinstance('1', int))


#3
x = 6
for i in range(2, x):
    if x % i == 0:
        print('不是素数')
        break
    else:
        print('是素数')

#检查10以内素数
x = 10
sum = 0
for i in range(2, x+1):
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            sum += 1
        print(sum)

#函数
def aplusB(a, b):
    c = a + b
    return a + b
result = aplusB(1, 2)
print(result)
print(aplusB(10, 12))

#圆面积
def circle(r):
    area  = r**2*3.14
    pi = 3.1415926
    return area, pi
area, pi(circle(5))
print(pi, area)


#命名函数
circle = lambda r, pi:r**2*pi
print(circle(3, 3.14))



#不可变对象
def change(a):
    a = 10
    b = 2
    change(b)
    print(b)



def main(x, *y):
    print(x)