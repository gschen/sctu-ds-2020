x=int(input("第一个数："))
y=int(input("第二个数："))
z=int(input("第三个数："))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(x,y,z)