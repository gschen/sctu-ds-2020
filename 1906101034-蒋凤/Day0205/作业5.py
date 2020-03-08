#5.（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x=int(input('请输入一个整数:'))
y=int(input('请输入一个整数:'))
z=int(input('请输入一个整数:'))
if x>y>z:
    print(z,y,x)
elif x>z>y:
    print(y,z,x)
elif y>x>z:
    print(z,x,y)
elif y>z>x:
    print(x,z,y)
elif z>x>y:
    print(y,x,z)
else:
    print(x,y,z)