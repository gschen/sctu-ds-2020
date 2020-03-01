def a(n):
    num=[]
    for i in range(1,n+1):
        if i%2==1:
            num.append(i)
        else:
            continue
    return num
print(a(7))
