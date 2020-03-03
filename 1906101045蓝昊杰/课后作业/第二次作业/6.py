def f(n):
    s=0
    if n%2==0:
        for i in range(2,n+1,2):
            s=s+1/i
    else:
        for i in range(1,n+1,2):
            s=s+1/i
    return s
print(f(4))