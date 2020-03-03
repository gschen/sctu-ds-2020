def BCY(n):
    s = 0
    if n == 1:
       return 1/1
    elif n==2:
       return 1/2
    else:
       return 1/n+BCY(n-2)
n = int(input("请输入一个数 ："))
print(BCY(n))