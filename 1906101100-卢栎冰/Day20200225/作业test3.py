# 3.（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表

# 样例输入
# 	1,2,3,4,5,6,7
# 样例输出
# 1, 3, 5, 7

# x=[1,2,3,4,5,6,7]
# def f(x):
#     return x=2*n+1
# print(x) 错的

def f(x):
    list=[]
    for i in range(len(x)):
        if i%2==1:
            list.append(x[i])
    return list
print(f([1,2,3,4,5,6,7,8,9]))

def f(x):
    list=[]
    for i in range(len(x)):
        if i%2==1:
