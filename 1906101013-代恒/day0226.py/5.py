def s(x):
    s1=0
    if x%2==0:
        n=2
        while n<=x:
            s1=s1+1/n
            n=n+2
        print(s1)
    else:
        n=1
        while n<=x:
            s1=s1+1/n
            n=n+2
        print(s1)

s(4)