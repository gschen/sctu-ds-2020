#用递归求n的阶乘

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fib(n-1)
print(fib(3))