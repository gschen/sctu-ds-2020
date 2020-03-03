x,y,z=map(int,input().split())
if y < x:
    x, y = y, x
if z < x:
    x, z = z, x
if z < y:
    y, z = z, y
print(x, y, z)