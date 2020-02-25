#集合
B=set('aabbbcg')
A={'a','b','c',1,'e'}
A.add('f')
print(A&B)
print(A,B)
print(A-B)
print(B-A)
print(A^B)

B.add(99)
print(B)

B.update({'l','o','v','e'},[99,88],'666')
print(B)

A.discard('f')
print(A.pop())
A.remove('b')
print(A)


#字典
d={'one':'I','two':'love','three':'You','five':'hahaha'}
print(d)

d['three']='He'
print(d)

d.get('one')

d.setdefault('four','Not Love They')
print(d)

del d['two']
print(d)

d.pop('five')
print(d)

d.popitem()
print(d)


#条件循环和判断
a=int(input('输入你的女朋友个数:'))
if a <= 1:
    print('羡慕死单身狗了!')
else:
    print('回家跪搓衣板吧!')


num1=20
num2=1
while (num1 != num2):
    num2=int(input('请输入你猜的数字:'))
    if (num2 != num1):
        print('猜错了!')
    else:
        print('恭喜猜对了')


num=int(input('请输入一个数字:'))
if num % 2 ==0:
    if num % 3 == 0:
        print('这个数字既能被2整除也能被3整除.')
    else:
        print('这个数能被2整除也不能被3整除。')
else:
    if num % 3 ==0:
        print('这个数能被3整除，不能被3整除')
    else:
        print('这个数不能被2和3整除')



sum=0
a=1
while a <= 100:
    sum=sum+a
    a=a+1
print(sum)




count=0
while count < 5:
    print(str(count),'<5')
    count = count+1
else:
    print(str(count)+'=5')



#
l=[1,2,3,4,5,6]
for i in l:
    print(i)


s='aasdfghg'
for i in s:
    print(i)



for i in range(1,10):
    print(i)

for i in range(1,20,2): 
    print(i)

print(list(range(5)))


#小练习1
l=[1,2,3,2,66]
a=l[0]
for i in l:
    if i > a:
        a=i
print(a)


#小练习2
l=[1,2,3,'a',1]
sum=0
for i in l:
    if isinstance(i,int):
        sum = sum+i
print(sum)


#小练习3
x=5
for i in range(1,x):
    if x % i ==0:
        print('不是素数')
        break
    else:
        print('是素数')


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
def lll(a,b):
    c=a+b
    return c


def circle_s(r):
    s=r**2*3.14
    return s
print(circle_s(3))


def circle_s(r,pi):
    s=r**2*pi
    return s
print(circle_s(5,3.14))



circle=lambda r,pi:r**2*pi
print(circle(3,3.14))



def change(a):
    a=10
b=2
change(b)
print(b)


l=[1,2,3,4]
def change(x):
    x.append([2,3,4])
    chenge(l)
print(l)


def ma(x,*y):
    print(x)
    print(y)
ma(1,1,1,1,1,1,1,1,11,1,1)
    