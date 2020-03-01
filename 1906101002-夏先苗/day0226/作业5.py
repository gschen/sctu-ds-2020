#（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x = int(input('第一个整数x：'))
y = int(input('第二个整数x：'))
z = int(input('第三个整数x：'))
if y > x:
    x, y = y, x
if z > x:
    x, z = z, x
if z > y:
    y, z = z, y

print(x, y, z)
