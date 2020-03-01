# 7.（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果.
def hi(x):
    a, b, c, d = 0, 0, 0, 0
    for i in x:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print('字母个数{},数字个数{},空格字数{},其他字符个数{}'.format(a, b, c, d))
hi(input('请输入一个字符串:'))
