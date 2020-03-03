'''4、求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
要求：n需要是input输入，且小于数组长度，不能固定。'''
nums = [14,25,98,75,23,1,4,56,59]
n = int(input())
def jiang(x):
    return x*x
print(sum(map(jiang,nums[:n])))