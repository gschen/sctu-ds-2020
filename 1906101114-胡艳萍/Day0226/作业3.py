# 3.（使用def函数完成）
# 找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表

def y(x):
    list=[]
    for i in range(len(x)):
        if i%2==0:
            list.append(x[i])
    return list
m=[1,2,3,4,5]
n=y(m)
print(n)