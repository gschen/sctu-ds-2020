#输入年龄，更具不同年龄来打印
age = int(input("输入年龄"))

if age >= 18:
    print("成年啦")
else:
    print("没有成年呢")


#猜数字大小游戏
num1 = 25
num2 = 1
while(num1 != num2):
    num2=int(input('输入一个数字：'))
    if num1>num2:
        print('你输入的值小了')
    elif num1<num2:
        print('你输入的值大了')
print('猜对啦！')



num = int(input("输入一个数字："))
if num % 2 ==0:
    if num % 3 ==0:
        print("这个数字既能被2整除也能被3整除")
    else:
        print("这个数字能被2整除，不能被3整除")
else:
    if num % 3  == 0:
        print("这个数字可以被3整除，不能被2整除")
    else:
        print("既不能被3整除，也不能被2整除")

    

#求1—100的和
sum = 0
a = 1
while(a <= 100):
    sum = sum + a
    a = a + 1
print(sum)


#无限循环
while():
    print("无限循环中！！！")




#运用while和else语句
count = 0

while count < 5:
    print(str(count),"<5")
    count = count + 1
else:
    print(str(count)+"=5")




#遍历
list = [1,2,3,4,5]
for i in list:
    print(i)



#打印双数
for i in range(0,11,3):
    print(i)


#打印列表
print(list(range(5)))




#给定一个列表找最大数
list = [1,2,3,2,6,10,1]
a = list[0]
for i in list:
    if i > a:
        a=i
print(a)

#计算数字列表之和
list = [1,2,3,4,'a',1]
sum=0
for i in list:
    if isinstance(i,int):#  print(isinstance(i,int))判断对象i是否为字符串，如果为真，会打印True，如为假,打印False。
        sum= sum + i
print(sum)


#检查给定数是否为素数（素数：一个大于1的正整数，如果除了1和它本身以外，不能被其他正整数整除，就叫素数。如2，3，5，7，11，13，17…。）
x = 6
for i in range:
    if x % i == 0: #计算除法的余数,是否x能够整除i,
        print ("不是素数")
        break
else:
    print("是素数")



#输入n，检查2-n之间有多少个素数。
x = 5
sum = 0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum = sum + 1
print(sum)




#函数
def AplusB(a,b):  #用户自定义函数名
    c=a+b       #代码块
    return c    #返回结果


#求圆半径
def circle(r):  #形参
    area=3.14*r**2
    return(area)
print(circle(4))


#实参
def circle(r=4):
    area=3.24*r**2
    return(area)
print(circle)

circle=lambda  r,pi:r**2*pi
print(circle(3,3.14))