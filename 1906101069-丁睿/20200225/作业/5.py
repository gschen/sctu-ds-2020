x,y,z=map(int,input("请输入3个整数:").split(","))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(x,y,z)