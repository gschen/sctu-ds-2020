# 2.（使用def函数完成）
# 编写一个函数，要求输入成绩，输出成绩的等级。
# 90-100为A，80-90为B，60-80为C，60分以下为D.

x=int(input('请输入你的成绩'))
def chengji(n):
    if n<=100:
        if n>=90:
            print('A')
        elif n>=80:
            print('B')
        elif n>=60:
            print('C')
        else:
            print('D')
chengji(x)