# （使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
# 样例输入
# D,a, ,s,1,3,2, ,a,2,d,a
# 样例输出
# 4, 6, 3, 0


def zhou(n):
    a,b,c,d=0,0,0,0
    for i in n:
        if i.isalpha():
            a=a+1
        elif i.isdigit():
            b=b+1
        elif i.isspace():
            c=c+1
        else:
            d=d+1
    print(a,b,c,d)
n=input()
zhou(n)