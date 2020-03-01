count = 0
lis=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k :
                count+=1
                lis.append(str(i)+str(j)+str(k))
print(count)
print(lis)