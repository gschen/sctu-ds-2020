#3.	（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表

def f1(p):
    li = []
    for i in range(len(p)):
        if i%2 == 0:
            li.append(p[i])
    return li
x = f1([1,2,3,4,5,6,7])
print(x)


