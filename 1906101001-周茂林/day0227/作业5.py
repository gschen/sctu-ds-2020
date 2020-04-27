'''
（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
'''
lis = set(list(map(int, input().split())))
print(' '.join(str(i) for i in lis))
