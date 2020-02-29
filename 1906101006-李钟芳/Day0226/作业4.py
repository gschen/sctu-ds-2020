'''4.（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''

l = ['1','2','3','4']
res = []
for a in l:
    for b in l:
        for c in l:
            if a != b and b != c and a != c:
                res.append(int(a+b+c))
print(len(res),'\n',res)
