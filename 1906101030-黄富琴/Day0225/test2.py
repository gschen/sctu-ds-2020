num=int(input('请输入一个数:'))
if num % 2 ==0:
    if num % 3 ==0:
        print('这个数既能被2整除也能被3整除')
    else:
        print('这个数能被2整除,不能被3整除')
else:
    if num % 3 ==0:
        print('这个数可以被3整除,不能被2整除')
    else:
        print('这个数既不能被3整除,也不能被2整除')
