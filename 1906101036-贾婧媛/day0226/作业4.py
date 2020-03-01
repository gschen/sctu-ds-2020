#4、（使用循环和判断）有四个数字：1、2、3、4
# 能组成多少个互不相同且无重复数字的三位数？各是多少？
list = ['1','2','3','4']
list1 = []
for a in list:
    for b in list:
        for c in list:
            if a!=b and b!=c and a!=c:
                list1.append(a+b+c)
print(len(list1),list1)