#条件循环和判断
age=int(input("请输入你的年龄："))
if age >= 18:
    print("你已经成年啦")
else:
    print("你还未成年")


# #猜数字游戏
num1=25
num2=1
while(num1 != num2):
    num2=int(input("请输入你的数字："))
    if num1 > num2:
        print("你输入的值太小了 ")
    elif num1 < num2:
        print("你输入的值太大了")
        print("猜对了")

num=int(input("请输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("这个数字既能被2整除也能被3整除")
    else:
        print("这个数字能被2整除，不能被3整除")
else:
    if num % 3 == 0:
        print("这个数字可以被3整除，不能被2整除")
    else:
        print("既不能被2整除，也不能被3整除")



sum=0
a=1
while(a <= 100):
    sum=sum+a
    a=a+1
print(sum)

while():
    print("无限循环中！！")


count=0
while count < 5:
    print(str(count),"<5")
    count=count+1
else:
    print(str(count)+"=5")

#for循环遍历
list1=[1,2,3,4,5]
for i in list1:
    print(i)

str1='abcdefg'
for j in str1:
    print(j)

for i in range(5):
    print(i)
for i in range(3,8):
    print(i)
for i in range(0,11,2):
    print(i)
print(list(range(5)))

#用for循环求最大值
list1=[1,2,3,4]
a=list1[0]
for i in list1:
    if i > a:
        a=i
print(a)

#用for循环求和
list2=[1,2,3,4,'a',1]
sum=0
for i in list2:
    if isinstance(i,int):
        sum=sum+i
print(sum)

#用for循环检查素数
x=6
for i in range(1,x):
    if x % i == 0:
        print("不是素数")
        break
else:
    print("是素数")

#
x=5
sum=0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
        else:
            sum=sum+1
print(sum)
