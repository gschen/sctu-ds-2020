def s(n):
    if n==1 or n ==0:
        return 1
    return n*s(n-1)
print(s(12)) 
