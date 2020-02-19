# coding=utf-8

'''
4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
要求：n需要是input输入，且小于数组长度，不能固定。
'''

l=[14,25,98,75,23,1,4,56,59]
n=int(input())
m=0
for i in l:
    if n>0:
        m+=i
        n-=1
    else:
        print(m)
        break