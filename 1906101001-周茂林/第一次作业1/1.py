'''
求给定数的阶乘
要求：所求阶乘的数不可以是这几个数：[1,10,20,30,40,50]。
'''


def aaa(n):
    if n == 0:
        return 1
    else:
        return n*aaa(n-1)


n = int(input())
list1 = [1, 10, 20, 30, 40, 50]
if n in list1:
    print('wrong----wrong')
else:
    print(aaa(n))
