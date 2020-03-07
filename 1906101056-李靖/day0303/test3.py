def r(n):
    sums=0
    if n%2==0:
        for i in range(2,n+1,2):
            sums=sums+(1/i)
            return sums
    else:
        for i in range(1,n+1,2):
            sums=sume+(1/i)
            return sums
print(r(6))