list1 = [1,2,3,2,6,10,1]#求出最大的数
a = list1[0]
for i in list1:
    if i > a:
        a=i
print(a)


list2 = [1,2,3,4,'a',1]#求数组中所有数字之和
sum=0
for i in list2:
    if isinstance(i,int):
        sum = sum + i
print(sum)


x=5#判断5是否为素数
for i in range(2,x):#如果for循环中没有出错和遇到break
    if x % i == 0:  #就会执行else
        print("不是素数")
        break
else:
    print("是素数")#该程序在VScode中不显示运行结果
                   #但代码是对的



x = 10#检查2到x之间有多少素数
sum=0
for i in range(2,x+1):
    for j in range(2,i):#第一次没有循环，i为2时
        if i % j == 0:  #range(2,2)
            break
    else:
        sum = sum +1
print(sum)#该程序在VScode中不显示运行结果
         #但代码是对的


age=int(input("请输入你的年龄:"))
if age >=18:
    print("你已经成年!")
else:
    print("你未成年!")#在VScode中运行不起，但代码无措


num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input("请输入你猜的数字："))
    if num1 > num2:
        print("你输入的值小了")
    elif num1 < num2:
        print("你输入的值大了")
print("猜对了")#在VScode中报错，但程序是对的



#if嵌套
num=int(input("请输入一个数字："))
if num % 2 ==0:
    if num % 3 == 0:
        print("这个数字既能被2整除也能被3整除")
    else:
        print("这个数字能被2整除，不能被3整除")
else:
    if num % 3 == 0:
        print("这个数字能被3整除,不能被2整除")
    else:
        print("这个数字既不能被3整除,也不能被2整除")#VScode中报错


#while循环
#求1到100 的和
sum=0
a = 1
while(a<=100):
    sum = sum + a
    a = a+1
print(sum)

#无限循环
a=1
while(a == 1):
    print("无线循环中！！！")

    
ocunt = 0
while count < 5:
    print(str(count),"<5")
    count = count + 1
else:
    print(str(count)+"=5")

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

print(list(range(5)))#创建列表