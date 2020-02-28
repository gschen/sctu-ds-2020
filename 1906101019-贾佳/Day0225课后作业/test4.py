sum = 0
for i in range(1,5):
    for s in range(1,5):
        for x in range(1,5):
            if i != s and i != x and s != x :
                sum +=1
                print("分别是",i,s,x)
print("共有：",sum,"个")