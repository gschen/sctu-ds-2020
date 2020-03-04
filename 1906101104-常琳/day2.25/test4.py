#（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

s=[1,2,3,4]
for a in s:
    for b in s:
        for c in s:
            if a!=b and a!=c and b!=c:
                print(a*100+b*10+c)