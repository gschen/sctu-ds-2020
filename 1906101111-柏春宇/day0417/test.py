def myfac(n):
    if n==1:
        return 1
    else:
        return myfac(n-1)*n
print(myfac(3))