num = int(input("请输入一个数字："))
if num %2 == 0:
    if num %3 == 0:
        print("这个数字既能被2整除也能被3整除")
    else:
        print("这个数字能被2整除但不能被3整除")
else:
    if num %3 == 0:
        print("这个数字不能被2整除但能被3整除")
    else:
        print("这个数字既不能被2整除也不能被3整除")