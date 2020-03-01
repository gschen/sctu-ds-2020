#（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
list = ['1','2','3','4']
for x in range(0,4):
    for y in range(0,4):
        for z in range(0,4):
            for c in range(0,4):
                if x!=y and x!=z and x!=c and y!=z and z!=c and y!=c:
                    print("{}{}{}{}".format(list[x],list[y],list[z],list[c]))
