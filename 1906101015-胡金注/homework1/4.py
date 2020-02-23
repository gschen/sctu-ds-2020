nums = [14,25,98,75,23,1,4,56,59]
n = int(input())
def L(x):
    return x*x
print(sum(map(L,nums[:n])))
