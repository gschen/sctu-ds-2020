x,y,z=map(int,input(),split())
if x>y>z:
    print(z,y,x)
elif x>z>y:
    print(y,z,x)
elif y>x>z:
    print(z,x,y)
elif y>z>x:
    print(x,z,y)
elif z>x>y:
    print(y,x,z)
else:
    print(x,y,z)