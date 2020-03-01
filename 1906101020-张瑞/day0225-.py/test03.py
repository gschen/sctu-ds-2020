num=int(input(''))
if num%2==0:
    if num%3==0:
        print('bei2,3zhengchu')
    else:
        print('bei2chu,bubei3chu')
else:
    if num%3==0:
        print('bei3chu,bubei2chu')
    else:
        print('既不被3整除，也不被2整除')
