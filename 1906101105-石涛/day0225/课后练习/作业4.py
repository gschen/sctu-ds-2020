# coding=utf-8

'''
4.	（使用循环和判断）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
l=[]
for i1 in [1,2,3,4]:
    for i2 in [1,2,3,4]:
        for i3 in [1,2,3,4]:
            l.append(str(i1)+str(i2)+str(i3))

print('能组成 {} 种三位数，各是：{}'.format(len(set(l)),set(l)))