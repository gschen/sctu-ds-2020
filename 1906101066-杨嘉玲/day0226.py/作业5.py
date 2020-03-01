x,y,z = eval(input("请输入三个整数并用‘,’隔开："))
if x > y:
    x,y = y,x
if x > z:
    x,z = z,x
if y > z:
    y,z = z,y
print(x,y,z)