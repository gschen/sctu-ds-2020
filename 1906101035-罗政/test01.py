age=int(input("请输入你的年龄"))
if age>=18:
    print("已经成年")
else:
    print("没有")

num1=25
num2=1
while(num1 !=num2):
    num2 = int(input("请输入数字："))
    if num1>num2:
        print("太小了")
    elif num1<num2:
        print("太大了")
#