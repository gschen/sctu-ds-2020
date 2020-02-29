#4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
l=[1,2,3,4]
a=0
for x in l:
    for y in l:
        for z in l:
            if x!=y and x!=z and y!=z:
                a=a+1
                print('%s%s%s'%(x,y,z))
print(a)