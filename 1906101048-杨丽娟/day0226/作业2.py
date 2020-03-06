'''2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。
90-100为A，80-90为B，60-80为C，60分以下为D.

样例输入
85
样例输出
B'''


def grade(n):
    if n<=100 and n>=90:
        return 'A'
    elif n<90 and n>=80:
        return 'B'
    elif n<80 and n>=60:
        return 'c'
    else:
        return 'D'
print(grade(98))
print(grade(88))
print(grade(70))
print(grade(50))