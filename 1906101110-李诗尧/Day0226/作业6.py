def a(n):
    s=0
    if n%2==0:
        for i in range(1,n+1,2):
            s=s+1/(i+1)
    else:
        for i in range(1,n+1,2):
            s=s+1/i
    return s
print(a(3))