count = 0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x!=y) and (x!=z) and(y!=z):
                count += 1
                print("%d%d%d"%(x,y,z),end=' ')
print("能组成%d个互不相同且不重复的三位数"%(count))
