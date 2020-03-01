age = int(input("请输入你的年龄"))

if age >= 18:
    print("你已经成年啦")
else:
    print("你还未成年")


num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input("请输入你猜的数字："))
    if num1 > num2:
        print("你输入的值小了")
    elif num1 < num2:
        print("你输入的值大了")