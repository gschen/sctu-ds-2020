num = int(input("请输入一个数字："))
if num % 2 ==0:
    if num % 3 == 0:
        print("这个数字既能被2也能被3整除")
    else:
        print("这个数字能被2整除，不能被3整除")
else:
    if num % 3 == 0:
        print("这个数字可以被3整除，不能被2整除")
    else:
        print("既不能被3整除，也不能被2整除")