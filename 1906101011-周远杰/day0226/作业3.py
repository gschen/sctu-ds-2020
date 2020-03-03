# （使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表


def zhou(*n):
    list1=[]
    for i in range(len(n)):
        if i%2==0:
            list1.append(n[i])
    return list1
print(zhou(1,2,3,4,5,6,7))