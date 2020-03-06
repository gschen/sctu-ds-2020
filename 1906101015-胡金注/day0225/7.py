def f(x):
    a, b, c, d = 0, 0, 0, 0
    for i in x :
        if i.isalpha():
            a += 1
        elif i.isdigit():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print('经统计:中英文字母{}个,数字{}个,空格{}个,其他字符{}个'.format(a,b,c,d))
f(list(input().split(',')))