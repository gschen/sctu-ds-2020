# coding=utf-8

'''
3.	（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表

样例输入
1,2,3,4,5,6,7
样例输出
1, 3, 5, 7
'''
def f(x):
    n=len(x)
    return x[0:(n+1):2]

m=eval(input())
print(str(f(m))[1:-1])