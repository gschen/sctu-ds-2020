#输入三个整数x,y,z，请把这三个数由小到大输出。
x = int(input('第一个整数：'))
y = int(input('第二个整数：'))
z = int(input('第三个整数：'))
lis1=[]
lis1.append(x)
lis1.append(y)
lis1.append(z)                        
for i in lis1:
    if x>y:
      x,y=y,x
    if y>z:
      y,z=z,y
    if x>z:
      x,z=z,x    
print(x,y,z)
          