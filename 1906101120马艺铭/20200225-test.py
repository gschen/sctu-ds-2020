A = ['a','b','c','c',1]

B=set('aabbcc')
#集合，交，并
print(A|B)
print(A&B)

print(A^B)


A.add('d')
print(A)

B.update([1,3],[4,2],'e')
print(B)


#删除元素
A = ['a','b','c','c',1]
A.remove('a')
A.remove('f')

A.discard('f')

A.pop()


# 字典
dic={'name':'张三'，'age':118,'school':'sctu'}
print(dic)
#修改数据
dic['name']='李四'
print(dic)
#查找数据
dic.get('name')

dic.setdefaul('address',defaul='成都')
print(dic)

#增加数据
dic['class']='3班'

#删除数据
del dic['name']
print(dic)

dic.pop('age')
print(dic)

dic.popitem()
print(dic)



age = int(input('请输入你的年龄'))
if age >= 18:
    print("你已经成年了")
else:
    print("你未成年")

num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input"请输入你猜的数字")
    if num1 > num2:
        print ("你输入的小了")
    elif  num1 < num2:
        print ("你输入的大了")
print("猜对了")



num  int(input("请输入一个数字："))
if num % 3 ==0:
    if num % 2 ==0:
        print("这个数能被2和3整除")
    else：print(这个数字能被2)
else:
    if num % 3 ==0:
        print("这数能被3")
    else:
        print ("既不能被3，也不能被2")


sum = 0
a = 1
while(a <= 100):
    sum = sum + a
    a = a + 1
print (sum)


while(a == 1):
    print("无限循环中！！！")


count = 0
while count < 5:
    print(count ,"<5")
    count = count + 1
else:
    print(str(count)+"-5")



list = [1,2,3,4,5]
for i in list1:
    print(i)

list2 = 'abcdefg'
for j in str1:
    print(j)



for i in range(5):
    print(i)

for i in range(2,10):
    print(i)


for i in range(0,11,2):
     print(i)


print(list(range(5)))

list = [1,2,3,2]


a = list[1]

for i in list1:
    if i > a:
        a = i
print(a)

list2  = [1,2,3,4,'a',1]

sum = 0
for i in list2:
    if isinstance(i,int):
        sum = sum + i
print(sum)



x = 5
for i in range(1,x):
    if x % i == 0:
        print("不是素数")
        break
else:
    print("素数")


x = 10
for i in range(2,x+1):
    for j in range(2,i):
        if i % j == 0:
            break 
    else:
        sum = sum + 1
print(sum)



def AplusB(a,b):

    return a+b
result=ApulsB(1,2)
print(result)
print(AplusB)



def circle(r):
    return r**2*3.14
print(circle(1))




a = 2
def main():
    b=3
    print(a)
main()
print(b)
 
