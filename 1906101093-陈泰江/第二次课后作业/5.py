x=int(input())
y=int(input())
z=int(input())
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x    
if y>z:
    y,z=z,y
print(x,y,z)        