#循环
age = int(input("请输入你的年龄"))
if age>=18:
    print('你已经成年')
else:
    print("你还未成年")

#猜数字
num1 = 25
num2 = 1
while(num1 != num2):
    num2 =int(input("请输入你猜的数字："))
    if num1 > num2:
        print("你输入的值小了")
    elif num1 < num2:
        print("你输入的值大了")
print('你猜对了')



num = int(input("请输入一个数字："))
if num % 2 ==0:
    if num % 3 == 0:
        print("这个数字既能被2整除也能被3整除")
    else:
        print("这个数字能被2整除，不能被三整除")
else:
    if num %3 == 0 :
        print("这个数字能被三整除，不能被二整除")
    else:
        print("既不能被三整除，也不能被二整除")