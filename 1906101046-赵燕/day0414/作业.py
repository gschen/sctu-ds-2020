def l(n):
    if n==1:
        return 1
    return n*lan(n-1)
print(l(5))
