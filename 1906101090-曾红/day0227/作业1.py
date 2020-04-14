#1（使用def函数完成）设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少
# def f(x):
#     return 3*x**4-9*x**2+x/2
# for x in [54,96,83,64,234,158,364]:
#     print(f(x))




#2（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.

# x=int(input("输入一个成绩"))
# def cj(x):
#     if 90<=x<=100:
#         print("A")
#     elif 80<=x<90:
#         print("B")
#     elif 60<=x<80:
#         print("C")
#     elif 0<=x<60:
#         print("D")
#     return
# print(cj(x))



# 3（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表

# l=[]
# def f(*x):
#     for i in range(len(x)):
#         if i%2==0:
#             l.append(x[i])
#     return l
# print(f(1,2,3,4,5,6,7))


# 4（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少
# l=[1,2,3,4]
# for a in l:
#     for b in l:
#         for c in l:
#             if a!=b and a!=c and b!=c:
#                 print(a*100+b*10+c)







#5（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出
# a=int(input("输入一个数"))
# b=int(input("输入一个数"))
# c=int(input("输入一个数"))
# if a>b>c:
#     print(c,b,a)
# elif a>c>b:
#     print(b,c,a)
# elif b>a>c:
#     print(c,a,b)
# elif b>c>a:
#     print(a,c,b)
# elif c>a>b:
#     print(b,a,c)
# else:
#     print(a,b,c)



# 6（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
# 样例输入
# D,a, ,s,1,3,2, ,a,2,d,a
# 样例输出
# 4, 6, 3, 0

l='D,a, ,s,1,3,2, ,a,2,d,a'
def f(x):
    a=0
    b=0
    c=0
    d=0
    for i in x:
        if i.isdigit():
            a +=1
        elif i.isalpha():
            b +=1
        elif i.isspace():
            c +=1
        else:
            d +=1
    return a,b,c,d
print(f(l))

