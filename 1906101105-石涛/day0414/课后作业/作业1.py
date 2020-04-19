# coding=utf-8

'''
用递归求n的阶乘
'''
n=eval(input())
def f(x):
    if x==1:
        return 1
    return x*f(x-1)
print(f(n))