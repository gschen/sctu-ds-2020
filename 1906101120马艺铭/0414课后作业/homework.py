def func(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * func(n - 1))


a = func(5)
print(a)