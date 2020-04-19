n=eval(input())
def fib(a=1,b=1,k=2):
    if k==n:
        return b
    return fib(b,a+b,k+1)

def fib1(n):
    if n==1 or n==2:
        return 1
    return fib1(n-1)+fib1(n-2)
print(fib1(5))



