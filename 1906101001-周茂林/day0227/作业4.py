'''
（使用循环和判断）
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
n = 0
lis = ['1', '2', '3', '4']
for i in range(123, 433):
    i = str(i)
    if len(set(i)) == 3 and max(i) < '5' and min(i) > '0':
        n += 1
        print(i)
print('共有{}个'.format(n))
