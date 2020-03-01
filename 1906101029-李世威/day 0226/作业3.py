#3.	（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
list=[]
def li(*x):
    for i in range(len(x)):
        if i%2==0:
            list.append(x[i])
    return list
print(li(1,2,3,4,5,6,7))
