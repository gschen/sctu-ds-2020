#用递归求n的阶乘

def h(n):
    if n==0 or n==1:
        return 1
    else:
        return n*h(n-1)
print(h(5))