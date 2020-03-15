#3、（使用def函数完成）找出传入函数的列表或元组的奇数位对应的元素，并返回一个新的列表 样例输入 1,2,3,4,5,6,7 样例输出 1,3,5,7

def he(*n):
    l1=[]
    for i in range(len(n)):
        if i%2==0:
            l1.append(n[i])
    return l1
print(he(1,2,3,4,5,6,7))
