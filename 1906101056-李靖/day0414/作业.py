def power(n):
    if n==0 or n==1:
        return 1
    else:
        return n*power(n-1)
print(power(3))