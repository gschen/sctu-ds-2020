#选做6
def wyh(x):
    R=0
    n=1
    m=2
    if x%2>0:
        while n<=x:
            R=R+1/n
            n=n+2
    else:
        while n<=x:
            R=R+1/m
            m=m+2
    print(R)