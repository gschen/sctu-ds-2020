def paritcall(n):
    if n%2==0:
        a=1/n
        while n>2:
            a=a+1/(n-2)
            n=n-2
        return a
    else:
        a=1/n
        while n>1:
            a=a+1/(n-2)
            n=n-2
        return a
n=eval(input('请输入一个大于0整数：'))
print(paritcall(n))