'''
（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。
90-100为A，80-90为B，60-80为C，60分以下为D.
'''
def grade(num):
    if 90<num<=100:
        return "A"
    elif 80<num<=90:
        return "B"
    elif 60<num<=80:
        return "C"
    elif 0<=num<=60:
        return "D"