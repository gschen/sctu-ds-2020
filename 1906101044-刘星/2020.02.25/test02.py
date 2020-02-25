#1
age=int(input("请输入你的年龄:"))
if age > 18:
    print("你已经成年了")
else:
    print("你还未成年")


#2
num = 25
num2 = 1
while (num != num2):
    num2 = int(input('请输入一个数字:'))
    if num > num2:
        print('你输入的值小了')
    elif num < num2:
        print('你输入的值大了')
    else:
        print('你猜对了')


#3
num = int(input("请输入一个数字:"))
if num % 2 == 0:
    if num % 3 == 0:
        print("这个数字既能被2整除，也能被3整除")
    else:
        print("这个数字能被2整除，不能被3整除")
else:
    if num % 3 == 0:
        print("这个数字能被3整除，不能被2整除")
    else:
        print("这个数既不能被2整除，也不能被3整除")


#4
sum = 0
a = 1
while (a <= 100):
    sum = sum + a
    a = a + 1
print(sum)


#5
count = 0
while count < 5:
    print(str(count),"< 5")
    count=count + 1
else:
    print(str(count)+"= 5")

#6
list1 = [1,2,3,4,5]
for i in list1:
    print(i)
str1 = 'abcde'
for j in str1:
    print(j)
for i in range(5):
    print(i)
for i in range (2,10):
    print(i)
for i in range(0,11,2):
    print(i)
print(list(range(5)))


#小练习

#给定一个列表，找列表中最大的元素
list = [1,2,3,4]
a = list[0]
for i in list:
    if i > a:
        a=i
print(a)

#计算列表中数字之和
list = [1,2,3,4,'a',5]
sum = 0
for i in list:
    if isinstance(i,int):
        sum = sum+i
print(sum)

#输入n，检查2到n之间有多少素数
x = int(input())
for i in range(2,x):
    if x % i ==0:
        print("不是素数")
        break
else:
    print("是素数")

x = 5
sum = 0 
for i in range(2,x+1):
    for j in range(2,i):
        if i %j == 0:
            break
    else:
        sum = sum+1
print(sum)