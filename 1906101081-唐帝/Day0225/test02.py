num=int(input('请输入一个数字：'))
if num%2==0:
    if num%3==0:
        print('这个数字既能被2整除，也能被3整除')
    else:
        print('这个数字只能被2整除，不能被3整除')
else:
    if num%3==0:
        print('这个数字不能被2整除，能被3整除')
    else:
        print('这个数字既不能被2整除，也不能被3整除')
        #