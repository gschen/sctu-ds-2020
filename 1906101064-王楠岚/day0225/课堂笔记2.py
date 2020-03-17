#条件判断
age=int(input("请输入你的年龄"))
if age >= 18:
    print("成年")
else:
    print("未成年")

num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input("请输入你猜的的数字"))
    if num1 > num2:
        print("大了")
    elif num1 < num2:
        print("小了")
    else:
        print("正确")

sum = 0
a = 1
while(a <= 100):
    sum = sum + a
    a = a + 1
print(sum)

while(a == 1):
    print("无限循环")

count = 0
while count < 5:
    print(str(count),"<5")
    count = count +1
else:
    print(str(count)+"=5")

list1=[1,2,3,4,5]
for i in list1:
    print(i)

str1='abcdefg'
for j in str1:
    print(j)

for c in range(5):
    print(c)

for q in range(2,10)
    print(q)

for w in range(1,11,3)
    print(w)

print(list(range(5)))

#第一题
list2=[1,2,3,4]
m=list2[0]
for n in list2:
    if n>m:
        m=n
print(m)
#第二题
list3=[1,2,3,4,'a',5]
sum=0
for i in list3:
    if isinstance(i,int):
    sum=sum+i
print(sum)
#第三题
x=6
for i in range(2,x):
    if x%i ==0:
        print('不是素数')
        break
else:
    print('是素数')

x=10
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum = sum + 1
print(sum)
