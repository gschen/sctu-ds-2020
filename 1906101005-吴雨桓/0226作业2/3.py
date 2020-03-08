def wu(x):
    l=[]
    for i in range(len(x)+1):
        if i % 2 == 1:
            l.append(x[i-1])
    print(l)

x = list(map(int,input().split()))
wu(x)
