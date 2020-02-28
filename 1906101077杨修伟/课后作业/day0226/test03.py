def yxw(*n):
    L=[]
    for i in n:
        a=n.index(i)
        if a%2 != 0:
            L.append(i)
    return L
print(yxw(1,2,3,4,5,6,7,8,9,0))