def yxw(n):
    a=1
    s=0
    if n%2==0:
        b=2
        while b<=n:
            c=a/b
            b=b+2
            s=s+c
        print(s)
    else:
        b=1
        while b<=n:
            c=a/b
            b=b+2
            s=s+c 
        print(s)
n=int(input())
yxw(n)
            