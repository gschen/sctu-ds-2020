# 1.	（使用def函数完成）设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.
# X取值：54,96,83,64,234,158,364
def f(*x):
    for x in x:
        f=3*4-9*2+x/2
        print(f)
f(54,96,83,64,234,158,364)

#  2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D
#
#  样例输入
# # 85
#  样例输出
# # B
def mark_s(x):
    if x>=90 and x<=100:
        return 'A'
    if x>=80 and x<90:
        return 'B'
    if x>=60 and x<80:
        return 'C'
    if x<60:
        return 'D'
x=int(input())
print(mark_s(x))

# 3.	（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
#
# 样例输入
# 	1,2,3,4,5,6,7
# 样例输出
# 1, 3, 5, 7
def li(*x):
    l=[]
    for i in x:
        if i%2!=0:
            l.append(i)
    return l
print(li(1,2,3,4,5,6,7))

# 4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and a!=c and b!=c:
                print('{}{}{}'.format(a,b,c))

# 5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x,y,z=input().split()
l=[x,y,z]
l.sort()
for i in l:
    print(i)
print(' ')

# 6.	（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
from fractions import Fraction
def method(n):
    sums=0
    if n%2==0:
        x=2
        while x<=n:
            sums+=Fraction(1,x)
            x+=2
        return sums
    else:
        x=1
        while x<=n:
            sums+=Fraction(1,x)
            x+=2
        return sums
print(method(7))

# 7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
# 样例输入
# D,a, ,s,1,3,2, ,a,2,d,a
# 样例输出
# 4, 6, 2, 0
def judge(*x):
    num_1=0
    num_2=0
    num_3=0
    num_4=0
    for i in x[0]:
        if i.isalpha():
            num_1+=1
        elif i.isdigit():
            num_2+=1
        elif i==' ':
            num_3+=1
        else:
            num_4+=1
    return '字母：{},数字：{},空格：{},其他：{}'.format(num_1,num_2,num_3,num_4)
print(judge(input().split(',')))