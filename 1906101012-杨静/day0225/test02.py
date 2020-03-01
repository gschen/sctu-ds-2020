#if语句 年龄
age = int(input("请输入你的年龄"))
if age >= 18:
    print("你已经成年啦")
else:
    print("你还未成年")

num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input("请输入你猜的数字："))
    if num1 > num2:
        print("你输入的值小了")
    elif num1 < num2:
        print("你输入的值大了")
print("猜对了")
#if嵌套
num= int(input("请输入一个数字："))
if num % 2 == 0:
    if  num % 3 == 0:
        print("这个数字既能被2也能被3整除")
    else:
        print("这个数字能被2整除，不能被3整除”)
else:
    if num % 3 == 0:
        print("这个数字可以被3整除，不能被2整除")
    else:
        print("既不能被3整除，也不能被2整除")

#循环语句
#while循环
#求1到100的和
sum=0
a = 1
while(a<=100):
    sum = sum + a
    a = a+1
print(sum)

#无限循环
while(a == 1):
    print("无限循环中！！！")

#
count = 0
while count < 5:
    print(str(count),"<5")
    count = count + 1
else:
    print(str(count)+"=5")

条件结构与循环小练习
#练习1
list=[1,2,3,2]
 a = lis[0]
for i in list1:
    if i > a:
        a=i
print(a)
#练习2
lis = [1,2,3,'a']
sum = 0
for i in lis:
    sum = sum + i
print(sum)
#练习3
x = 5
sum= 0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
        else:
            sum = sum + 1
print(sum)

#函数

#for循环
list1 = [1,2,3,4,5]
for i in list1:
    print(i)

str1 = "abcdefg"
for i in str1:
    print(i)

for i in range(5):
    print(i)

for i in range(2,10):
    print(i)

for i in range(0,11,2):
    print(i)

for i in range(0,11,3):
    print(i)
print(list(range(5)))
'''1、给定一个列表,找列表中最大的元素
输入：[1,2,3,2]
输出：3'''

list1 = [1,2,3,2]

a = list1[0]

for i in list1:
    if i > a:
        a = i
print(a)

'''2、计算列表中数字之和
输入：[1,2,3,"a",1]
输出：7'''#print(isinstance(1,int))判断1和int数字类型是不是一样的，一样返回ture，不一样换回false

list2 = [1,2,3,"a",1]

sum = 0

for i in list2:
    if isinstance(i,int):
        sum = sum + i
print(sum)

'''3、输入n，检查2-n之间有多少个素数（质数是大于1（不包括1）的自然数，除1及其本身外，没有除数。）
输入：5
输出：3
原因：1-5，素数有2，3，5'''

'''x = 5
for i in range(2,x):
    if x % i == 0:
        print("不是素数")
        break
else:
    print("是素数")'''

x = 10
sum = 0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum = sum + 1
print(sum)