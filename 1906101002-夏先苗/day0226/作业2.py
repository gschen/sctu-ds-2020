# （使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.
# 样例输入
# 85
# 样例输出
# B
def grade(n):
    if 80<=n<90:
        return 'B'
    if 90<=n<=100:
        return 'A'
    else:
        if 60<=n<80:
            return 'C'
        if 0<n<60:
            return 'D'
print(grade(50))
print(grade(84))
print(grade(92))
print(grade(70))

        
    