#4. 重组
a=[1,2,3,4]
n=0
for i in a:
    for ii in a:
        for iii in a:
            if len(set([i,ii,iii]))==3:
                n+=1
print(n)
