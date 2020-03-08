#（使用def函数完成）设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.
#X取值：54,96,83,64,234,158,364
def f(x):
    return 3 * x ** 4 - 9 * x ** 2 + x / 2
for x in list[54,96,83,64,234,158,364]

#（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.

#样例输入
#85
#样例输出
#B
n = input('请输入一个成绩：')
def cj():
    if n < 100 and n >= 90:
        print('A')
    elif n < 90 and n >= 80:
        print('B')
    elif n < 80 and N >= 60:
        print('C')
    else:
        print('D')

#（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表

#样例输入
	#1,2,3,4,5,6,7
#样例输出
#1, 3, 5, 7
x = input()
def ds(x):
    list=[]
    if x % 2 == 0:
        list.append(x)
    return list

#（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
list=[]
for A in range(1,5):
    for B in range(1,5):
        for C in range(1,5):
            if A != B and B != C and C != A:
                list.append(A*100+B*10+C)
n=len(list)
print("一共有%d个数，各是:%s"%(n,list))
#（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x = input()
y = input()
z = input()
if y < x:
    x,y = y,x
if z < x:
    x,z = z,x
if z < y:
    y,z = z,y
print(x,y,z)