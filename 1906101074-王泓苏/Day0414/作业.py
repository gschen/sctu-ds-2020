def func(n):
    if n==1:
        return 1
    return n*func(n-1)
a=func(5)
print(a)