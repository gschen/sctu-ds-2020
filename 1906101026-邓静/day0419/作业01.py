def H(n):
    if n==0 or n==1:
        return 1
    else:
        return H(n-1)*n
print(H(7)) 
