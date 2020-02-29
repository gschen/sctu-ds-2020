#集合
A={'a','b','c','c','1'}
B=set(aabbcce)
print(A-B)
print(A|B)
print(A&B)
print(A^B)
A.add('a')
B.update({1,3},{4,2},'e')
A.remove('a')
A.discard('f')
A.pop.()


#字典
dic={'name':'张三','age':'19','school':,'sctu'}
#修改数据
dic['name']='李四'
#查找数据
dic.get('name')
#dic.setdefault('address', default='成都')
#增加数据
dic['class']='3班'
#删除数据
del dic['name']
dic.pop('age')
dic.pop()

#if循环
age = int(input("请输入你的年龄："))

if age >=18:
    print("你已经成年了")
else:
    print("你还没有成年")


num = int(input("请输入一个数:"))
if num % 3 == 0:
    print("这个数字可以被2整除，也可以被3整除")
else:
    if num %3 == 0:
        print("这个数字可以被3整除，不能被2整除")
    else:
        print("这个数字不能被3整除，不能被2整除")


#while循环
sum = 0
a = 1
while(a <= 100):
    sum = sum + 1
    a = a + 1
print(sum)

# while():
#     print("无限循环中！！！")

count= 0
while count < 5:
    print(str(count),"<5")
    count = count + 1
else:
    print(str(count) + '5')

#for循环

list1 = [1,2,3,4,5]
for i in list:
    print(i)

str1 = 'abcdefg'
for j in str1:
    print(i)

for i in range(5):
    print(i)

for i in range(2,5):
    print(i)

for i in range(0,11,2):
    print(i)

print(list(range(5)))



list1 = [1,2,3,2]
a = list1[0]
for i in list1:
    if i > a:
        a = i
print(a)

list2 = [1,2,3,4,'a',1]
sum = 0
for i in list2:
    if isinstance(i,int):
        sum = sum +i
print(sum)

list3 = [1,2,3,,2]
a=list3[0]
for i in list3:
    if i > a:
        a = i
print(a)

x=5
for i in range(2,x):
    if x%i==0:
        print('不是素数')
        break
    else:
        print('是素数')

x=10
sum=0
for i in range(2,x+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=1
print(sum)


a=2
def main():
    b= 3
    print(a)
main()
print(b)

def circle(r):
    area = r**2*3.14
    pi = 3.1415926
    return area,pi
area,pi=circle(5)
print(pi,area)


def change(a):
    a=10
b=2
change(b)
print(b)
