def xwx(n):
    if n%2==0:

        return ou(n)
    else:
        return ji(n)

def ji(n):
    sums=0
    for i in range(1,n+1,2):
        sums+=1/i
    return sums
def ou(n):
    sums=0
    for i in range(2,n+1,2):
        sums+=1/i
    return sums
print('{:.2f}'.format(xwx(3)))