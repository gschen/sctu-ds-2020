# （使用def函数完成）写函数，统计字符串中有几个字母，
# 几个数字，几个空格，几个其他字符，并返回结果



def zhou(n):
    a,b,c,d=0,0,0,0
    for i in n:
        if i.isalpha():
            a=a+1
        elif isinstance(i,str):
            b=b+1
        elif i.isspace():
            c=c+1
        else:
            d=d+1
    print("%d,%d,%d,%d" % (a,b,c,d))
if __name__ == '__main__':
    n=input()
    zhou(n)