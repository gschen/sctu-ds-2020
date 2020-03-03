print('请输入3个数:')
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
a = 0
if x>y:
    a=y
    y=x
    x=a
if x>z:
    a=z
    z=x
    x=a
if y>z:
    a=z
    z=y
    y=a
print("这3个数由小到大输入的结果是：",x,y,z)
