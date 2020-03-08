# 5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x,y,z=input().split()
l=[x,y,z]
l.sort()
for i in l:
    print(i,end=' ')
print(' ')
