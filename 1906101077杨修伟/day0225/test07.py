def yxw(n):
    a=0
    b=0
    c=0
    d=0
    for i in n:
        if i.isalpha():
            a=a+1
        if i.isdigit():
           b=b+1
        if i.isspace():
            c=c+1
        else:
            d=d+1
    print("字母:%d,数字:%d,空格:%d,其他:%d"%(a,b,c,d))
n=input()
yxw(n)

