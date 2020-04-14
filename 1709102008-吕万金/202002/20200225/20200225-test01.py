A={'a','b','c','c',1}
B=set('aabbcce')
print(A,B)
#并
print(A|B)
#交
print(A&B)
#补
print(B-A)
#不同时包含
print(A^B)


#增
A.add('d')
#A.add('a') 操作没有意义
print(A)
B.update({1,3},[4,2],'e')
print(B)

#删
#clear全删
#discard删除指定
A.remove('a')
print(A)
#A.remove('f')会报错，因为不存在
A.discard('f')#不会报错
print(A)
A.pop()#随机删
print(A)


#字典 键唯一，值多样
dic={'name':'张三','age':19,'school':'sctu'}
print(dic)
#修改数据
dic['name']='李四'
#查找数据
dic.get('name')
#dic.setdefault('address','成都') 类似于get，若不存在重新定义一个键为fault
print(dic)
#增加数据
dic['class']='2班'
#删除数据
del dic['name']
#dic.pop('age')
#dic.popitem()删除最后一对键值
print(dic)


#条件循环
age=int(input('输入你的年龄'))
if age>=18:
    print('你已经成年')
else:
    print('你尚未成年')


num1=25
num2=1
while num1!=num2:
    num2=int(input('输入猜测的数字：'))
    if num1> num2:
        print('小了')
    elif num1<num2:
        print('大了')
print('猜对了')

#if嵌套
num=int(input('输入一个数字：'))
if num%2==0:
    if num%3==0:
        print('这个数字能被2也能被3整除')
    else:
        print('这个数字能被2整除不能被3整除')
else:
    if num %3==0:
        print('这个数字能被3整除却不能被2整除')
    else:
        print('既不能被3整除也不能被2整除')



sum=0
a=1
while a<=100:
    sum+=a
    a+=1
print(sum)

while a==1:
    print('无线循环ing')

c=0
while c<5:
    print(str(c),'<5')
    c+=1
else:
    print(str(c)+'-5')

l1=[1,2,3,4,5]
for i in l1:
    print(i)

l2='abcefdgag'
for k in l2:
    print(k)

for g in range(5):
    print(g)
for g in range(2,10):
    print(g)
for g in range(0,11,2):
    print(g)

print(list(range(5)))


l3=[1,2,3,2]
a=l3[0]
for i in l3:
    if i>a:
        a=i
print(a)

l4=[1,2,3,4,'a',1,'b',21]
sum=0
for i in l4:
    if isinstance(i,int):
        sum+=i
print(sum)

x=5
for i in range(2,x):
    if x%i==0:
        print('不是素数')
        break
else:
    print('素数')

x=10
sum=0
for i in range(2,x+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=1
print(sum)

#实例
def cir(r):
    area=3.14*r**2
    pi=3.14159265
    return area,pi
area,pi=cir(5)
print(area,pi)

# a=2
# def main():
#     b=3
#     print(a)
# main()
# print(b)
#lambda
cir=lambda r,pi:r**2*pi
print(cir(3,3.14))

def change(a):
    a=10
b=2
change(b)
print(b)  


        