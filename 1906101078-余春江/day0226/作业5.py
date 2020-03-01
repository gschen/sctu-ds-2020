# （使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x = int(input("请输入正整数x:"))
y = int(input("请输入正整数y:"))
z = int(input("请输入正整数z:"))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(x,y,z)