# age=int(input('请输入你的年龄'))
# if age >= 18:
#    print('你成年了')
# else:
#    print('你还未成年')    

num1 = 25
num2 = 1
while(num1 != num2):
    num2 = int(input('请输入一个数字:'))
    if num1 > num2:
        print('太小了')
    elif num1 < num2:
        print('太大了')
print('猜对了')