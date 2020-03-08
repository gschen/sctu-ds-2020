l=[1,2,3,4]
l2=[]
n=0
for i in l:
    for j in l:
        for k in l:
            if i != j and i != k and j != k:
                l2.append("%d%d%d"%(i,j,k))
                n+=1
print(n,l2)