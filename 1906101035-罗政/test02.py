num =int(input("请输入一个数字:"))
if num%2==0:
    if num%3==0:
     print("这个数字可以被2和3整除")
    else:
        print("这个数字可以被2整除，不能被3整除")
else:
    if num%3==0:
        print("这个可以被3整除，不可以被2整除")
    else:
         print("都不可以")