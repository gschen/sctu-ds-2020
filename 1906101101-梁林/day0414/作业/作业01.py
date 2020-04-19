#n的阶层
n=int(input())
def stratum(x):
    if x==1:
        return x
    else:
        return x*stratum(x-1)
print(stratum(n))