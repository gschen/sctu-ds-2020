# coding=utf-8

'''
5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
'''
l=[]
for i in range(3):
    m=int(input())
    l.append(m)
for i in range(2):
    if l[i]>l[i+1]:
        a,b=l[i],l[i+1]
        l[i],l[i+1]=b,a
for i in range(2):
    if l[i]>l[i+1]:
        a,b=l[i],l[i+1]
        l[i],l[i+1]=b,a
print('%d<%d<%d' % (l[0],l[1],l[2]))