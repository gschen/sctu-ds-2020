#5. （使用循环和判断）输入三个整数x,y,z，请把这三个数由小到大输出。
x,y,z=map(int,input().split())
if x>y>z:
    print(z,y,x)
elif x>z>y:
    print(y,z,x)
elif y>x>z:
    print(z,x,y)
elif y>z>x:
    print(y,x,z)
elif z>x>y:
    print(y,x,z)
elif z>y>x:
    print(x,y,z)

