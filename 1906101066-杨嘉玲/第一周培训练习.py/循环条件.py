#while循环
num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input("请输入数字："))
    if num1 > num2:
        print("偏小")
    elif num1 < num2:
        print("偏大")
print("对了") 

#while..else..
count = 0
while count < 5:
    print(str(count)+"<5")
    count = count + 1
else:
    print(str(count)+"=5")

#求1-100的和
sum = 0
a = 1
while(a <= 100):
    sum = sum + a
    a = a + 1
print(sum)

#if..else..
age = int(input("请输入你的年龄："))
if age > 18:
    print("你已成年")
else:
    print("你未成年")

num = int(input("请输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("这个数字既能被2整除，也能被3整除")
    else:
        print("这个数能被2整除，不能被3整除")
else:
    if num % 3 == 0:
        print("这个数字可以被3整除，不能被2整除")
    else:
        print("这个数既不能被2整除也不能被3整除")

#for
#for
list1 = [1,2,3,4,5]
for i in list1:
    print(i)

list2 = ['abcdefg']
for x in list2:
    print(x)  

for j in range(5):
    print(j)

for h in range(0,10,2):
    print(h)

#可创建列表
print(list(range(5)))

#小练习
#1.给定一个列表，找列表中最大的元素
list = [1,2,3,,4]
a = list[0]
for i in list:
    if i > a:
        a = i
print(a)

#2.计算列表中数字之和
list = [1,2,3,4,'a',5]
sum = 0
for i in list:
    if isinstance(i,int):
        sum = sum + i
print(sum)

#3.输入n,检查2-n之间素数个数
x = int(input("请输入："))
for i in range(2,x):
    if x % i == 0:
        print("不是素数")
        break
else:
    print("是素数")

 x = int(input("请输入："))
 sum = 0
 for i in range(2,x+1):
     for j in range(2,i):
         if i % j == 0:
             break
    else:
        sum = sum + 1
print("输出：%sum"%sum)



