# 用递归求n的阶层
# n!=(n-1)!*n=(n-2)!*(n-1)*n=1*(n-a)*…..*(n-2)*(n-1)*n

def f(x):
    if x==1:
        return 1
    return x*f(x-1)

print(f(5))