#7.（使用def函数完成）写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
#样例输入
#D,a, ,s,1,3,2, ,a,2,d,a
#样例输出
#4, 6, 3, 0

def f(x):
    a,b,c,d=0,0,0,0
    for i in x:
        if ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122:
            a+=1
        elif ord(i)>=48 and ord(i)<=57:
            b+=1
        elif ord(i)==32:
            c+=1
        else:
            d+=1
    return ('字母有%d个，数字有%d个，空格有%d个，其它字符有%d个'%(a,b,c,d))
x=input().split(',')
print(x)
print(f(x))