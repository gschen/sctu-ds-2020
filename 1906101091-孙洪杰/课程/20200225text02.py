age=int(input("请输入你的年龄:"))

if age >=18:
    print("你已经成年了")
else:
    print("你还未成年")


num1=25
num2=1
while(num1 !=num2):
    num2=int(input(" 请输入你猜的数字:"))
    if num1>num2:
        print("你输入的值小了")
    elif num1<num2:
        print("你输入的值大了")
print("猜对了")



#if嵌套
num=int(input("请输入一个数字:"))
if num%2==0:
    if num%3==0:
        print("这个数字既能被2整除,也能被3整除")
    else:
        print("这个数字能被2整除,不能被3整除")
else:
    if num%3==0:
        print("这个数字可以被3整除,不能被2整除")
    else:
        print("这个数字既不能被2整除,也不能被3整除")


#循环语句
#sum=0
#a=1
#while(a<=100):
#    sum=sum+a
#    a=a+1
#print(sum)

#while(a==1):
#    print("无限循环中！！！")

#while循环
count=0

#while count<5:
#    print(str(count),"<5")
#    count=count+1
#else:
#    print(str(count)+"=5")

#for循环
#list1=[1,2,3,4,5]
#for i in list1:
#    print(i)
#str1='abcdefg'
#for j in str1:
#    print(j)

#for i in range(5):
#    print(i)


#for i in range(2,10):
#    print(i)

#for i in range(0,11,3):
#    print(i)

#print(list(range(5)))

#1
list1=[1,2,3,2]
a=list1[0]
for i in list1:
    if i>a:
        a=i
print(a)

#2
list2=[1,2,3,4,'a',21]
sum=0
for i in list2:
    if isinstance(i,int):
        sum=sum+i
print(sum)

#3
x=5
for i in range(1,x):
    if x%i==0:
        print("不是素数")
        break
else:
    print("是素数")


x=10
for i in range(2,x+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum=sum+1
print(sum)


def ApulusB(a,b):
    return a+b
result=ApulusB(1,2)
print(result)
print(ApulusB(10,12))


def circle(r):
    return r**2*3.14
print(circle(5))

a=2
def main():
    b=3
    print(a)
main()
print(b)

circle3=lambda r,pi:r**2*pi
print(circle3(3,3.14))

def change(a):
    a=10
b=2
change(b)#a=b=10
print(b)

c=[1,2,3]
def change2(x):
    x.append([1,2,3])
change2(c)
print(c)

b='123'
b=123

def main(x,*y):
    print(x)
    for i in range(len(y)):
        print(y[i])
main(1,11,12,13,14)










