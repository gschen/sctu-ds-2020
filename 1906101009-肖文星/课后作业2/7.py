def xwx(n):
    a, b, c, d = 0, 0, 0, 0
    for i in n:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            b += 1
        elif i==' ':
            c += 1
        else:
            d += 1
    return '英文{} 数字{} 空格{} 其他{}'.format(a, b, c, d)
print(xwx('D,a, ,s,1,3,2, ,a,2,d,a'))