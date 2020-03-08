'''5.（使用循环和判断）输入三个整数x,y,z
，请把这三个数由小到大输出。'''
x = int(input())
y = int(input())
z = int(input())
if y < x:
    x,y = y,x
if z < x:
    x,z = z,x
if z < y:
    y,z = z,y
print(x,y,z)


#解法二:
x,y,z=map(int,input().split())
ls=[x,y,z]
ls.sort()
print(ls)