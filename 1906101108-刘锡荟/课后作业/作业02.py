#1

def f(x):
     y = 3*(x**4) - 9*(x**2) + x/2
     return y
list=[54,96,83,64,234,158,364]
for i in list:
    print(f(i),end = ' ')

#2

def grade(x:int):
    if x >= 90:
         return 'A'
    if 90 > x >= 80:
         return 'B'
    if 80 >x>= 60:
         return 'C'
    if x < 60:
         return 'D'
x = int(input('请输入成绩：'))
print('成绩的等级：{}'.format(grade(x)))

#3

N = list(map(int,input("请输入列表(各数之间用“,”隔开)：").split(',')))
for i in N:
    if i %2 == 0:
       N.remove(i)
print("已知列表奇数位所组成的新列表：{}".format(N))

#4

list = ['1','2','3','4']
l = []
for i in list:
    for j in list:
        for k in list:
            a = i+j+k
            if a not in  l:
                l.append(a)
print("能组成{}个互不相同且无重复数字的三位数".format(len(l)))
for i in l:
    print(i,end = ' ')


#5

a = list(map(int,input("输入三个整数x,y,z并用“,”隔开：").split(',')))
a.sort()
for i in a:
    print(i,end = ' ')

#6

def ou(n):
    s = 0
    for i in range(2,n+1,2):
        s += 1/i
    return s
def ji(n):
    s = 0
    for i in range(1,n+1,2):
        s += 1/i
    return s
n = int(input("请输入一个整数："))
if n%2 == 0:
    print(ou(n))
else:
    print(ji(n))

#7
s = input('请输入一行字符串：')
a = []
b = []
c = []
d = []
for i in iter(s):
    if i.isalpha():
        a.append(i)
    elif i.isdigit():
        b.append(i)
    elif i.isspace():
        c.append(i)
print("英文字符：{}个数：{},数字：{}个数:{},空格：{}个数：{},其它字符：{}个数：{}".format(len(a),len(b),len(c),len(d)))

