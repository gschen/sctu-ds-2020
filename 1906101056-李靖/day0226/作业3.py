#3
def jishu(l1):
    l2 = []
    for i in range(len(l1)):
        if i % 2 == 0: 
            l2.append(l1[i])
    return l2
l3 = [1,2,3,4,5,6,7]
print(jishu(l3))