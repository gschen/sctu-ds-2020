def abc(n):
    if n==1:
        return 1
    return n*abc(n-1)
print(abc(10))