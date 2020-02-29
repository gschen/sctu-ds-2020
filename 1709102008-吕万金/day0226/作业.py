'''1.	（使用def函数完成）设f(x)=3x4-9x2+x/2，
请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.
X取值：54,96,83,64,234,158,364
'''
def f(x):
    return 3*4-9*2+x/2
print(f(54),f(96),f(83),f(64),f(234),f(158),f(364))

'''2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。
90-100为A，80-90为B，60-80为C，60分以下为D.
样例输入
85
样例输出
B
'''
def grade(n):
    if n<=100 and n >90:
        return 'A'
    elif n<=90 and n>80:
        return 'B'
    elif n<=80 and n>60:
        return 'C'
    else:
        return 'D'
print(grade(85))

'''3.	（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，
并返回一个新的列表
样例输入
	1,2,3,4,5,6,7
样例输出
1, 3, 5, 7
'''
l1=[1,2,3,4,5,6,7]
print(l1[::2])

'''4.	（使用循环和判断）有四个数字：1、2、3、4，
能组成多少个互不相同且无重复数字的三位数？各是多少？'''

l2=[]
for a in [1,2,3,4]:
    for b in [1, 2, 3, 4]:
        for c in [1, 2, 3, 4]:
            if a!=b and b!=c and c!=a:
                l2.append(a*100+b*10+c)
print(len(l2))
print(l2)
'''5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。'''
x,y,z=map(int,input().split())
l=[x,y,z]
l.sort()
print(l)
'''6.	（使用def函数完成）编写一个函数，输入n为偶数时，
调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n'''
def num(n):
    s=0
    if n%2==0:
        for i in range(2,n+1,2):
            k=1/i
            s+=k
        return s
    else:
        for ii in range(1,n+1,2):
            kk=1/ii
            s+=kk
        return s
print(num(4))
print(num(5))
'''7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，
几个空格，几个其他字符，并返回结果
样例输入
D,a, ,s,1,3,2, ,a,2,d,a
样例输出
4, 6, 3, 0
'''
def list(n):
    letter=[]
    number=[]
    spare=[]
    other=[]
    for k in n:
        if k==' ':
            spare.append(k)
        elif k in range(0,10):
            number.append(k)
        elif k.isalpha():
            letter.append(k)
        else:
            other.append(k)
    return len(letter),len(number),len(spare),len(other)
print(list(['D','a',' ','s',1,3,2,' ','a',2,'d','a']))
