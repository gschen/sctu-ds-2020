#2.（使用def函数完成）编写一个函数，要求输入成绩，输出成绩的等级。90-100为A，80-90为B，60-80为C，60分以下为D.
def garde(c):
    if c in range(90,100):
        print("等级为A")
    if c in range(80,90):
        print("等级为B")
    if c in range(60,80):
        print('等级为C')
    if c <= 60 :
        print('等级为D')
c=int(input("请输入成绩："))
garde(c)