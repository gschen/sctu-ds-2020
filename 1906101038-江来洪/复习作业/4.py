nums = [14,25,98,75,23,1,4,56,59]
n = int(input())
def jiang(x):
    return x*x
print(sum(map(jiang,nums[:n])))
