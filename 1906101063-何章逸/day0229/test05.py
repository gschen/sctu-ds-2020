#5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
a,b,c=map(int,input().split())
l=[a,b,c]
l.sort()
print(l)
