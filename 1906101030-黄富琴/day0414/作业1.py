def jc(n):
    if n==0 or n==1:
        return 1
    else:
        return jc(n-1)*n
print(jc(3))