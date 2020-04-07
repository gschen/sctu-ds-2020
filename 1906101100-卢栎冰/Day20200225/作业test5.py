# 5.（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。

x=int(input('输入第一个整数'))
y=int(input('输入第二个整数'))
z=int(input('输入第三个整数'))
if x>y:
    x,y=y,x
if y>z:
    y,z=z,y
if x>z:
    x,z=z,x
print(x,y,z)
