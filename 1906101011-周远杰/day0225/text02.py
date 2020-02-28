# def APluSB(a,b):
#     return a+b
# result =APluSB(1,2)
# print(result)

# def circle(r):
#     return r**2*3.14
# print(circle(5))
# print(circle(10))

# a=2
# def main():
#     b=3
#     print(a)
# main()
# print(b)
"""
#lambda函数：格式；变量名=lambda 参数1 参数2 返回
circle=lambda r,pi:r**2*pi
print(circle(3,3.14))


age=int(input("请输入你的年龄"))
if age>=18:
    print("已经成年")
else:
    print("没有")

num1=25
num2=1
while(num1 !=num2):
    num2 = int(input("请输入数字："))
    if num1>num2:
        print("太小了")
    elif num1<num2:
        print("太大了")


num =int(input("请输入一个数字:"))
if num%2==0:
    if num%3==0:
     print("这个数字可以被2和3整除")
    else:
        print("这个数字可以被2整除，不能被3整除")
else:
    if num%3==0:
        print("这个可以被3整除，不可以被2整除")
    else:
         print("都不可以")


sum=0
a=1
while a<=100:
    sum+=a
    a=a+1
print(sum)

while():
    print("无线循环")

count=0
while count<5:
    print(str(count)"<5")
    count=count+1
else:
    print(str(count)"=5")


list=[1,2,3,4]
for i in list:
    print(i)

str="abcdefg"
for j in str:
    print(j)

for i in rang(2,5):
    print(i)


for i in rang(1,10,2):
    print(i)


list=[1,2,3,4]
a=list[0]
for i in list:
    if i>a:
        a=i
print(a)

list=[1,2,3,4,'a']
sum=0
for i in list:
    if isinstance(i,int):
        sum+=i
print(sum)
"""
x=5
for i in range(2,x):
    if x%i==0:
        print("不是")
        break
else:
    print("是")
#判断是不是素数