x,y,z=map(int,input("请输入三个数字，数字间用空格隔开:").split())
if x<y<z:
    print(x,y,z)
elif x<z<y:
    print(x,z,y)
elif y<x<z:
    print(y,x,z)
elif y<z<x:
    print(y,z,x)
elif z<y<x:
    print(z,y,x)
else:print(z,x,y)