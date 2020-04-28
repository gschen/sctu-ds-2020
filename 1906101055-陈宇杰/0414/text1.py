n=eval(input())
def fib(a=1, b=1,k=2):
    if k==n:
       return b
    return fib(b, a+b,k+1)
print(fib())
