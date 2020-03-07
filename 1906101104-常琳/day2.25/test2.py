#2.（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.
#样例输入:85
#样例输出：B

x=eval(input(''))
def g(x):
    return x
if x>=90 and x<=100:
    print('A')
elif x>=80 and x<90:
    print('B')
elif x>=60 and x<80:
    print('C')
else:
    print('D')