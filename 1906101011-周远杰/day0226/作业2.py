# （使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。
# 90-100为A，80-90为B，60-80为C，60分以下为D.


def zhou(n):
    if 90<=n<=100:
        return 'A'
    elif n >= 80:
        return 'B'
    elif n >= 60:
        return 'C'
    else:
        return 'D'
n=int(input("请输入一个成绩："))
print(zhou(n))