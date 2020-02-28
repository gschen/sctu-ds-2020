#6.（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

def f(n):
    s=0
    if n%2 == 0:
        for i in range(2,n+1,2):
            x = 1/i
            s = s+x
        print(s)
    else:
        for i in range(1,n+1,2):
            x = 1/i
            s = s+x
        print(s)
n=int(input('输入一个整数：'))
f(n)    