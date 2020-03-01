#6.（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，
# 调用函数1/1+1/3+...+1/n

def f(n):
    a=1
    s=0
    if n%2==0:
        b=2
        while b<=n:
            c=a/b
            b=b+2
            s=s+c
        print(s)
    else:
        b=1
        while b<=n:
            c=a/b
            b=b+2
            s=s+c 
        print(s)
n=int(input())
f(n)