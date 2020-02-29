'''4.（使用循环和判断）有四个数字：1、2、3、4，能组成
多少个互不相同且无重复数字的三位数？各是多少？'''
L=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and b!=c and c!=a:
                L.append(a*100+b*10+c)
n=len(L)
print("一共有%d个数，各是:%s"%(n,L))