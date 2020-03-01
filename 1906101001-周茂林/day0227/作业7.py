'''
（使用def函数完成）
写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
样例输入
D,a, ,s,1,3,2, ,a,2,d,a
样例输出
6, 4, 2, 0
'''
def bbb(sr):
    a, b, c, d = 0, 0, 0, 0
    for i in sr:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print('经统计:中英文字母{}个,数字{}个,空格{}个,其他字符{}个'.format(a,b,c,d))


bbb(list(input().split(',')))
