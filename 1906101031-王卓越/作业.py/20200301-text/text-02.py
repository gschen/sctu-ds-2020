# 2.	（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.

# 样例输入
# 85
# 样例输出
# B
def mark_s(x):
    if x>=90 and x<=100:
        return 'A'
    if x>=80 and x<90:
        return 'B'
    if x>=60 and x<80:
        return 'C'
    if x<60:
        return 'D'
x=int(input())
print(mark_s(x))
