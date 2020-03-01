'''
（使用def函数完成）
设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.
X取值：54,96,83,64,234,158,364
'''
def f(x):
    return 3*x**4 - 9*x**2 + x/2

for x in [54, 96, 83, 64, 234, 158, 364]:
    print(f(x))


'''
（使用def函数完成）
编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.
样例输入
85
样例输出
B
'''
def main(n):
    if 90 <= n <= 100:
        return 'A'
    elif 80 <= n < 90:
        return 'B'
    elif 60 <= n < 80:
        return 'C'
    elif n < 60:
        return 'D'


print(main(int(input())))


'''
（使用def函数完成）
找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
样例输入
[1,2,3,4,5,6,7]
样例输出
1, 3, 5, 7
'''
def mai(lis):
    lis1 = []
    le = len(lis)
    for i in range(0, le, 2):
        lis1.append(lis[i])
    return lis1

print(mai(eval(input())))


'''
（使用循环和判断）
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
n = 0
lis = ['1', '2', '3', '4']
for i in range(123, 433):
    i = str(i)
    if len(set(i)) == 3 and max(i) < '5' and min(i) > '0':
        n += 1
        print(i)
print('共有{}个'.format(n))


'''
（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
'''
lis = set(list(map(int, input().split())))
print(' '.join(str(i) for i in lis))


'''
（使用def函数完成）
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''
def aaa(n):
    sum = 0
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            sum += 1/i
        return sum
    else :
        for i in range(1, n+1, 2):
            sum += 1/i
        return sum


print(aaa(int(input())))


'''
（使用def函数完成）
写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
样例输入
D,a, ,s,1,3,2, ,a,2,d,a
样例输出
6, 4, 2, 0
'''
def bbb(sr):
    a, b, c, d = 0, 0, 0, 0
    for i in sr:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print('经统计:中英文字母{}个,数字{}个,空格{}个,其他字符{}个'.format(a,b,c,d))


bbb(list(input().split(',')))
