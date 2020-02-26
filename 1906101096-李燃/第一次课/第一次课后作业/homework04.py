#求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定

from functools import reduce

l1=[14,25,98,75,23,1,4,56,59]
def square_of_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum

n = int(input('输入一个数值：'))
print(square_of_sum(n))