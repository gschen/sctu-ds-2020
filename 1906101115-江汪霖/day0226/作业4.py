L=[1,2,3,4]
a = 0
for i in L:
    for j in L:
        for k in L:
            if i != j and i != k and j != k:
                a = a + 1 
                print('%d%d%d'%(i,j,k))
print('%d个这样的三位数'% a )