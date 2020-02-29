l=[14,25,98,75,231,4,56,59]

n=int(input())

def wu(x):
    return x**2

print(sum(map(wu,l[:n])))