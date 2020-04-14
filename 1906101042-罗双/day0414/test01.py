#1.递归：斐波拉契数列
#程序上：值函数调用自身的过程
#递归必须有终止条件

#斐波拉契数列
n=eval(input())
'''
def fib(a=1,b=1,k=2):
    if k==n:
        return b
    return fib(b,a+b,k+1)
print(fib())
'''

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(n))