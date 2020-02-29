#2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.
#样例输入：85  样例输出：B

x =int(input('请输入成绩：'))
def g(x):
    if x<=100 and x>=90:
        return 'A'
    elif x<=90 and x>=80:
        return 'B'
    elif x<80 and x>=60:
        return 'C'
    else:
        return 'D'
print(g(x))