age = int(input('请输入你的年龄'))
if age >=18:
    print('你已成年')
else:
    print('你还未成年')


num1=25
num2=1
while(num1 !=num2):
    num2=int(input('请输入你猜的数字：'))
    if num1>num2:
        print('你输入的数字小了')
    elif num1<num2:
        print('n你输入的数字大了')
print('你猜对了')


num=int(input('请输入一个数字：'))
if num % 2 ==0:
    if num % 3 ==0:
        print('这个数字既能被2也能被3整除')
    else:
        print('这个数字能被2整除，不能被3整除')
else:
    if num % 3 ==0:
        print('这个数字可以被3整除，不能被2整除')
    else:
        print('既不能被3整除，也不能被2整除')



sum=0
a=1
while(a<=100):
    sum=sum+a
    a=a+1
print(sum)

while(a):
    print('无限循环中！！！')



count=0
while count<5:
    print(str(count),'<5')
    count=count +1
else:
    print(str(count)+'=5')


#for循环
list1=[1,2,3,4,5]
for i in list1:
    print(i)


str1='abcdef'
for j in str1:
    print(j)


for i in range(5):
    print(i)


for i in range(2,10):
    print(i)


for i in range(0,11,2):
    print(i)


print(list(range(5)))



list1=[1,2,3,2]
a=list1[0]
for i in list1:
    if i >a:
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

