def jiang(l):
    res = []
    for i in range(len(l)+1):
        if i % 2 == 1:
            res.append(l[i-1])
    return res
l = list(map(int,input().split()))
print(jiang(l))