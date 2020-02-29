#4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
l=[1,2,3,4]
n=0
for x in l:
    for y in l:
        for z in l:
            if (x!=y) and (y!=z) and (z!=x):
                n+=1
                print(x,y,z)
print('能组成%d个'%(n))
