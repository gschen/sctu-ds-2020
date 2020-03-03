A = ["a", "b", "c", 1]
B = ['aabbcce']
print(A - B)  # 补
print(A | B)  # 并
print(A & B)  # 交
print(A ^ B)  # 不同时包括

# 字典
dic = {'name': '张三', 'age': '18,'}
dic['name'] = "李四"
print(dic)
# 查找数据
dic.get
dic.setdefault('address', '成都')
# 增加数据
dic['class'] = '1班'
# 删除数据
del dic['name']
dic.pop['name']
# 删除最后一个
dic.popitem()

age = int(input("请输入您的年龄："))

if age >= 18:
    print('你已经成年')
else:
    print('你没有成年')

num1 = 25
num2 = 1
while (num1 != num2):
    num2 =

sum = 0
a = 1
while (a <= 100):
    sum = sum + a
    a = a + 1
print(sum)

l = [1, 2, 3, 4, 5]
for i in l:
    print(i)

for i in range(2, 10, 2):
    print(i)

list = [1, 2, 3, 5, 2, 10]

a = list[0]
for i in list:
    if i > a:
        a = i
print(a)

sum = 0
list2 = [1, 5, 7, 'a']
for i in list2:
    if isinstance(i, int):
        sum = sum + i
print(sum)

x = 6
for i in range(2, x):
    if x % i == 0:
        print('不是素数')
        break
else:
    print('是素数')


def zxc(r):
    return r ** 2 * 3.14


print(zxc(6))

a = 2


def zxc():
    b = 3
    print(a)


zxc()
print(b)