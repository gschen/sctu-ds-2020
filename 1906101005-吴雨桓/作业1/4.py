l=[14,25,98,75,231,4,56,59]  #求前N个数的平方，N需要输入

n=int(input())

def wu(x):
    return x**2

print(sum(map(wu,l[:n])))