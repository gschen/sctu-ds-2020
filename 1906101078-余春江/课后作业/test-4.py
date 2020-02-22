#求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
list = [14,25,98,78,23,1,4,56,59]
n = int(input())
def args(x):
    return x*x
print(sum(map(args,list[:n])))
