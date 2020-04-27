# （使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
# 当输入n为奇数时，调用函数1/1+1/3+...+1/n


def zhou(n):
    if n%2==0:
        a=0
        sum1=0
        for i in range(2,n+1,2):
            sum1=sum1+1/i
            a=a+1
        print(sum1)
    else:
        b=0
        sum2=0
        for i in range(1,n+1,2):
            sum2=sum2+1/i
            b=b+1
        print(sum2)
n=int(input())
zhou(n)