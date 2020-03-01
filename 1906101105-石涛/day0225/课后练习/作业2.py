# coding=utf-8

'''
2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.

样例输入
85
样例输出
B
'''
def f(x):
    if x>=90:
        return 'A'
    elif x>=80:
        return 'B'
    elif x>=60:
        return 'C'
    elif x<60:
        return 'D'
m=int(input())
print(f(m))