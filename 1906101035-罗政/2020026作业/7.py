"""
7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
样例输入
D,a, ,s,1,3,2, ,a,2,d,a
样例输出
4, 6, 3, 0
"""
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