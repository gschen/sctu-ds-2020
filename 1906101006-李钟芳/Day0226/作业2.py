'''2.（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.

样例输入
85
样例输出
B'''

def lizhongfang(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 60 <= grade < 80:
        return 'C'
    else:
        return 'D'
grade = int(input())
print(lizhongfang(grade))

