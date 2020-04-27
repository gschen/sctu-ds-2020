#2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.

#样例输入
# 85
# 样例输出
# B
def sxy(n):
    if n<60:
        print("D")
    elif 60<=n<80:
        print("C")
    elif 80<=n<90:
        print("B")
    elif 90<=n<=100:
        print("A")
n=int(input("输入一个数字:"))


