#1.	（使用def函数完成）设f(x)=3x4-9x2+x/2，请将f(x)封装为一个函数，求当x等于以下值时，f(x)是多少.X取值：54,96,83,64,234,158,364

#def adu(x):
#    result = 3*x**4-9*x**2+x/2
#   print(result)
#adu(54)

#2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.

#def grade(c):
#    result = c
#    if result < 60:
#        return 'D'
#    elif result < 80:
#        return 'C'
#    elif result < 90:
#        return 'B'
#    else:
#        return 'A'
#print(grade(40))

#3.	（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
#l = []
#def num(n):
#    for i in range(len(n)):
#        if i % 2 == 0:
#            l.append(n[l])
#    return l
#ol =  num([1,2,3,4,5])
#print(ol)

#4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#n=0
#for a in range(1,5):
#    for b in range(1, 5):
#        for c in range(1, 5):
#            if a != b and b != c and c != a:
#                n+=1
#                print(a,b,c)

#5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
#x=input('x:')
#y=input('y:')
#z=input('z:')
#if x > y:
#    x,y = y,x
#if x > z:
#    x,z = z,x
#if y > z:
#    y,z = z,y
#print(x,y,z)

#7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
#n=input('请输入：')
#for i in list:
#   if i.isdigit():
#        int_count += 1
#    elif i.isalnum():
#        str_count += 1
#else:
#    other_count += 1
#print('数字=%d,字母=%d,其它=%d'%(int_count,str_count,other_count))#

