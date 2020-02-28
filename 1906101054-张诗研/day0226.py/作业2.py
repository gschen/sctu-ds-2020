# 2.编写一个函数，要求输入成绩，输出成绩的等级。
# 90-100为A，80-90为B，60-80为C，60分以下为D.
x=eval(input("请输入成绩："))
def f(x):
    if 90<=x<=100:
        print("A")
    elif 80<=x<90:
        print("B")
    elif 80<=x<=90:
        print("C")
    else:
        print("D")
    return x    
print(f(x))
    