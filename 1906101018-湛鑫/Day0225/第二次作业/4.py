# 4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

h=[1,2,3,4]
c=0
for a in h:
    for b in h:
        for c in h:
            if(a!=c) and (a!=b) anf (b!=c):
                print(a,b,c)