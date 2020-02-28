#4.（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
l=[1,2,3,4]
l1=[]
for a in l:
    for b in l :
        for c in l :
            if a != b and b != c and c != a:
                d = a*100+b*10+c
                l1.append(d)
n=len(l1)
print("能组成%d个数，各是%s:"%(n,l1))