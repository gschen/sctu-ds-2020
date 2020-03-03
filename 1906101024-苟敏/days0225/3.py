li = []
def jishu(n):
    for i in range(len(n)):
        if i % 2 == 0:
            li.append(n[i])
    return li
ret = jishu([1,2,3,4,5,6,7])
print(ret)