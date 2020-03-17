#4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
l1=[1,2,3,4]
i=0
for x in l1:
    for y in l1:
        for z in l1:
            if x!=y and x!=z and y!=z:
                i+=1
            print(x*100+y*10+z)
print(i)