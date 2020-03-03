#4. （使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
m=[1,2,3,4]
i=0
for a in m:
 for b in m:
    for c in m:
        if a!=b and a!=c and b!=c:
            i=i+1
            print(a*100+b*10+c)
print("能组成%d个"%(i))

