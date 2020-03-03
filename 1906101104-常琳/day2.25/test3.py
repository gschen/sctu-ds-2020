#使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
#样例输入:1,2,3,4,5,6,7
#样例输出:1, 3, 5, 7

s=[1,2,3,4,5,6,7]
c=[ ]
def f(x):
    for i in range(len(s)):
        if (i-1)%2==0:
            pass
        else:
            c.append(s[i])
    return c
m=f(s)
print(len(s))
print(m)


def g(x):
    return x[::2]
print(g([1,2,3,4,5]))