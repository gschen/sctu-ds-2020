# 用递归求n的阶层
# n!=(n-1)!*n=(n-2)!*(n-1)*n=1*(n-a)*…..*(n-2)*(n-1)*n
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fib(n-1)
print(fib(5)) 
print(fib(12))