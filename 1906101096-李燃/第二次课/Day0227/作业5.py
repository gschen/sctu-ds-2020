#（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(input("请输入第一个数："))
y = int(input("请输入第二个数："))
z = int(input("请输入第三个数："))
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)