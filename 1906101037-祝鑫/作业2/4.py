'''
（使用循环和判断）
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
l=[1,2,3,4]
n=0
for a in l:
    for b in l:
        for c in l:
            if a!=b and a!=c and b!=c:
                n+=1
                print(a*100+b*10+c)


print("共有%d个数"%(n))