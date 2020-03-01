#3.找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表
def f(x):
    li1=[]
    for i in range(len(x)):
        if i%2==1:
            li1.append(x[i])
    return li1
print(f([1,2,3,4,5,6,7]))