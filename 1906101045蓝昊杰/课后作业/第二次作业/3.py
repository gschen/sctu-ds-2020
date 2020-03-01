def f(x):
    l=[]
    n=len(x)
    for i in range(0,n+1,2):
        l.append(x[i])
    return l
print(f([1,2,3,4,5,6,7]))