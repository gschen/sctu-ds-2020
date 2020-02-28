#7.	（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
#样例输入
#D,a, ,s,1,3,2, ,a,2,d,a
#样例输出
#4, 6, 3, 0

def mjj(x):
    a=0
    b=0
    c=0
    d=0
    for i in x:
        if i.isalpha():
            a=a+1
        if i.isdigit():
            b=b+1
        if i.isspace():
            c=c+1
        else:
            d=d+1
    print('字母=%s,数字=%s,空格=%s,其他=%s'%(a,b,c,d))
x=input('请输入一段字符：')
mjj(x)