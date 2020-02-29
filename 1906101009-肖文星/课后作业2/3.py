def xwx(a):
    lis=[]
    b=len(a)
    for i in range(0,b,2):
        lis.append(a[i])
    return lis
print(xwx([1,2,3,4,5,6,7]))