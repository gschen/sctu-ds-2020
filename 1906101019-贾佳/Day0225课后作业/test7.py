def N(x):
    a,b,c,d=0,0,0,0
    for i in x:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            b+=1
        elif i.isspace():
            c+=1
        else:
            d+=1
    return '英文字符数{},数字字符数{},空格字符数{},其他字符数{}'.format(a,b,c,d)
x = input()
print(N(x))