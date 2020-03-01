L=[1,2,3,4]
s=0
for i in L:
    for j in L:
        for k in L:
            if len(set(i,j,k))==3:
                print("%s%s%s"%(i,j,k),end=" ")
                s +=1
print("最终的结果为：%s个"%s)                
