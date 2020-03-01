A={'a','b','c','c',1}
B=set('aabbccc')
print(A,B)
print(B-A)
print(A/B)
print(A&B)
print(A^B)

A.add('a')
B.update({1,3},[4,2],'e')
print(A)
print(B)

A.remove('a')
A.remove('f')
A.discard('f')

A.pop()
print(A)

dic={'name':'张三','age':19,'school':'sctu'}
print(dic)
dic['name']='李四'
dic.get('name')
dic.setdefault('address','成都')
dic['class']='1班'
del dic['name']
dic.pop('name')
dic.popitem()
print(dic)

age=int(input('请输入年龄：'))
if age >= 18:
    print('你已经成年了')
else:
    print('未成年')

num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input('请输入你猜的数：'))
    if num1 > num2:
        print('小了')
    elif num1 < num2:
        print('大了')
print('对了')





num = int(input('输入:'))
if num % 2 == 0:
    if num % 3 == 0:
        print('能被2，3整除')
    else：
        print('能被2整除')
else:
    if num % 3 ==0:
        print("能被3整除")
    else:
        print('不能被2，3整除')




sum = 0
a = 1
while(a <= 100):
    sum += a
    a += 1
print(sum)
while(a == 1):
    print('无限循环')

count = 0

while count = 0:
    print(str(count),'<5')
    coyunt += 1
else:
    print(str(count)+'=5')


list1 = [1,2,3,4,5]
for i in list1:
    print(i)

str1 = 'abcdefg'
for j in str1:
    print(j)


for i in range(5):
    print(i)

for i in range(2:10):
    print(i)


print(list(range(5)))


list2 = [1,2,3,2]
a = list2[0]
for i in list2:
    if i > a:
        a = i
print(a)

list3 = [1,2,3,4,'a',1]
sum = 0
for i in list3:
    if isinstance(i,int):
        sum += i
print(sum)


x = 5
for i in range(1,x):
    if x%i == 0:
        print('不是素数')
        break
else:
    print('是素数')




x = 10
sum = 0
for i in range(2:x+1):
    for j in range(2:i):
        if i%j == 0:
            break
    else:
        sum += 1
print(sum)



def s(r):
    return r**2*3.14
print(s(5))








