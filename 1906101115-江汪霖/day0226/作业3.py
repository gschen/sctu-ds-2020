def b(*a):
    L=[]
    for i in a:
        x = a.index(i)
        if x % 2 !=0:
            L.append(i)
    return L
print(b(1,2,3,4,5,6,7))


