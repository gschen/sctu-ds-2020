#集合
A={'a','b','c',1}
B=set('aabbcce')
#并
print(A|B)
#交
print(A&B)
#差（补）
print(A-B)
print(B-A)
#不同时包含
print(A^B)
#为几个添加元素，当存在时不添加。
A.add('d')
print(A)
#增加元素，参数可以是列表、元素、字典
B.update({1,3},[4,2],'e')
print(B)
#移除指定元素，元素不在时会报错
A.remove('a')
A.remove('f')
#移除指定元素，元素不在时不会报错
A.discard('f')
#随机移除元素,并返回被删除的元素
B.pop()
print(B)
#字典(键必须唯一，值可以多样)
d={'name':'张三','age':19,'school':'sctu'}
print(d)
#修改数据
d['name']='李四'
#查找数据
d.get('address')
d.setdefaul
t('name')
#增加数据
d['class']='1班'
print(d)
#删除数据 前两种必须写出
#del dic['name']   删除键值和value
#删除并返回删除的value   d.pop('age')
print(d)
#删除最后一个值
d.popitem()
print(d)

#条件判断
age=int(input("请输入你的年龄"))
if age >= 18:
    print("成年")
else:
    print("未成年")

num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input("请输入你猜的的数字"))
    if num1 > num2:
        print("大了")
    elif num1 < num2:
        print("小了")
    else:
        print("正确")

sum = 0
a = 1
while(a <= 100):
    sum = sum + a
    a = a + 1
print(sum)

while(a == 1):
    print("无限循环")

count = 0
while count < 5:
    print(str(count),"<5")
    count = count +1
else:
    print(str(count)+"=5")

list1=[1,2,3,4,5]
for i in list1:
    print(i)

str1='abcdefg'
for j in str1:
    print(j)

for c in range(5):
    print(c)

for q in range(2,10)
    print(q)

for w in range(1,11,3)
    print(w)

print(list(range(5)))

#第一题
list2=[1,2,3,4]
m=list2[0]
for n in list2:
    if n>m:
        m=n
print(m)
#第二题
sum=0
list3=[1,2,3,4,'a',5]
for i in list3:
    if isinstance(i,int):
    sum=sum+i
print(sum)
#第三题
x=6
for i in range(2,x):
    if x%i ==0:
        print('不是素数')
        break
else:
    print('是素数')

x=10
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum = sum + 1
print(sum)

#函数
def AplusB(a,b):
    return a+b
result=AplusB(1,2)
print(result)

def circle(r):
    return r**2*3.14
print(circle(5))


def circle(r=6):
    a=r**2*3.14
    return a
print(circle)