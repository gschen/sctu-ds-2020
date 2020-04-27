#4.（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
counter=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j != k !=i:
                print("%d%d%d"%(i,j,k))
                counter +=1             
print("共有%d种组合"%(counter))