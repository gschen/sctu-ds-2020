#if条件语句：以及常用的操作符(>、<、<=、>=、==、!=)
age=int(input('输入你的年龄：'))
if age>=18:
    print('已成年')
else:
    print('未成年')

#while和if同时使用
num1=2
num2=5
while num1!=num2:
    num2=int(input('输入你所猜测的数字：'))
    if num1>num2:
        print('你猜测小了')
    else:
        print('你猜测大了')
print('你猜测对了')

#if嵌套：判断能否被2、3整除
num=int(input('输入数字:'))
if num%2==0:
    if num%3==0:
        print('这个数字能被2和3同时整除')
    else:
        print('这个数字可以被2整除，但是不能被3整除')
else:
    if num%3==0:
        print('这个数字不能被2整除，可以被3整除')
    else:
        print('这个数字不能被2和3整除')



