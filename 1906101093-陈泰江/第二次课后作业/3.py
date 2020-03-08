def f1(p):
    li = []
    for i in range(len(p)):
        if i % 2 != 0:
            li.append(p[i])
    return li
ret = f1([1,2,3,4,5,6,7])
print(ret)