# 用递归求n的阶层
def fib(n):
    if n==1:
        return 1
    else:
        return fib(n-1)*n

print(fib(5))