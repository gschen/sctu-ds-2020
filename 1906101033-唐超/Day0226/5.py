#5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x,y,z=map(int,input().split())
if y < x:
    x,y = y,x
if z < x:
    x,z = z,x
if z < y:
    y,z = z,y
print(x, y, z)