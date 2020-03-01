def intro(n):
    if n >= 90 and n < 100:
        print("你的成绩等级为A")
    elif n >= 80 and n < 90:
        print("你的成绩等级为B")
    elif n >= 60 and n < 80:
        print("你的成绩等级为C")
    else:
        print("你的成绩等级为D")
n = int(input("请输入你的成绩："))
result = intro(n)
 