#2.（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.
#样例输入85
#样例输出B

def grede():
    score = float(input('请输入你的成绩：'))
    if score<60:
        print("D")
    elif score<80:
        print("C")
    elif score<90:
        print("B")
    else:
        print("A")
    
grede()
#输入85