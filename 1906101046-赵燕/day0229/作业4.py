list=[1,2,3,4]
a=0
for x in list:
    for y in list:
        for z in list:
            if x!=y and x!=z and y!=z:
                a=a+1
                print("%d%d%d"%(x,y,z))
print("一共有%d"%(a))