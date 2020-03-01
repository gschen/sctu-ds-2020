L=[1,2,3,4]
s=0
for i in L:
    for j in L:
        for k in L:
            if i != j and i != k and j != k:
                s=s+1
                print("%d%d%d"%(i,j,k))
print(s)