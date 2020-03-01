#5.	（使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x=int(input('请输入一个整数：'))
y=int(input('请输入一个整数：'))
z=int(input('请输入一个整数：'))
if x>y>z:
    print(x,y,z)
elif x>z>y:
    print(x,z,y)
elif y>x>z:
    print(y,x,z)
elif y>z>x:
    print(y,z,x)
elif z>x>y:
    print(z,x,y)
else:
    print(z,y,x)
