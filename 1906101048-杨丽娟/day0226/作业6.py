'''6.	（使用def函数完成）编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
当输入n为奇数时，调用函数1/1+1/3+...+1/n'''
def math(n):
    sum=0
    if n%2==0:
        for i in range(1,n+1):
            a=1/(2*i)
            sum=sum+a
        return sum
    else:
        for m in range(1,n+1):
            b=1/(m-1)
            sum=sum+b
        return sum
print(math(5))
print(math(6))

