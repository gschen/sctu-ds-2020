x = int(input("请输入正整数："))
y = int(input("请输入正整数："))
z = int(input("请输入正整数："))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(x,y,z)