#2.（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.
x=int(input('请输入你的成绩：'))
def grade(x):
    if x>=60:
        if 80>x>=60:
            return('C')
        if 90>x>=80:
                return('B')
        if 100>=x>=90:
            return('A')
    else:
        return('D')
print(grade(x))