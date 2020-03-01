#（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
list = (1,2,3,4,5,6,7)
def lb(list):
    X = list[::2]
    print(X)
print(lb(list))