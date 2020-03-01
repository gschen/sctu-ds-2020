#条件判断
#用if语句实现：根据输入的年龄判断是否成年
age=int(input('请输入你的年龄：'))
if age<18:
    print('未成年！')
else:
    print('成年！')
#用if语句(&if嵌套)实现：猜数字大小游戏
num1=1
num2=23
num1=int(input('请输入一个数：'))
if num1>=num2:
    if num1==num2:
        print('猜对了')
    else:
        print('太大了')
else:
    print('太小了')
    
    
#循环
#while循环：求1到100的和
sum=0
a=1
while a<=100:
    sum=sum+a
    a=a+1
print(sum)
#无限循环
# while (a==1):
#     print('无限循环！')
#while循环使用else语句
count=0
while count<5:
    print(str(count),'<5')
    count=count+1
else:
    print(str(count),'=5')
#for循环
for i in range(3):
    a=list(range(3))
print(a)


#小练习
#求列表中最大元素
lis1=[1,2,3,2]
lis1.sort()
print(lis1[-1])

lis1=[1,2,3,2]
a=lis1[0]
for i in lis1:
    if i>a:
        a=i
print(a)

lis1=[1,2,3,2]
print(max(lis1))

#计算列表中数字之和   
lis2=[1,2,3,'a',1]
sum=0
for i in lis2:
    if isinstance(i,int):
        sum=sum+i
print(sum)

#输入n,检查2~n之间素数的个数
x=int(input('请输入一个数n:'))
sum=0
for i in range(2,x+1):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        sum=sum+1
print(sum)
