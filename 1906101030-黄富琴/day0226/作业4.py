n=0
for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
            if (i!=j) and (i!=m) and (j!=m):
                n +=1
                print(i,j,m)
print(n)
                
