# coding=utf-8
'''
1、	求给定数的阶乘
要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。
'''

l=[1,10,20,30,40,50]
x=int(input())
if x not in l:
    def jc(i):
        if i==1:
            return 1
        return i*jc(i-1)
    print(jc(x))