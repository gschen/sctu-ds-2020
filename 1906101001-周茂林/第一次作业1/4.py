'''
求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
要求：n需要是input输入，且小于数组长度，不能固定。
'''


def ddd(x):
    return x*x


list1 = [14, 25, 98, 75, 23, 1, 4, 56, 59]
n = int(input())
if n >= len(list1):
    print('n不小于数组的长度,不符合题意')
else:
    print(sum(map(ddd, list1[:n])))
