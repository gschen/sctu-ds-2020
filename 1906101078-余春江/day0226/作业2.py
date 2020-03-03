#（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.
x = int(input("请输入一个成绩："))
def cj(x):
    if x<60:
        return "D"
    elif x<80:
        return "C"
    elif x<90:
        return "B"
    else:
        return "A"
print(cj(x))