#2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.
def li(x):
    if x<60:
        print('D')
    elif 60<=x<80:
        print('C')
    elif 80<=x<90:
        print('B')
    elif 90<=x<=100:
        print('A')
x=int(input('请输入成绩：'))
li(x)
