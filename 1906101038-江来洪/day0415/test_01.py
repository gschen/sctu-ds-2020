def jiang(n):
    if n == 0:
        return 1
    return jiang(n-1)*n
n = int(input())
print(jiang(n))