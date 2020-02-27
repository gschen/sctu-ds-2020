nums = [14,25,98,75,23,1,4,56,59]
n = int(input())
def squre(x):
    return x*x
print(sum(map(squre,nums[:n])))