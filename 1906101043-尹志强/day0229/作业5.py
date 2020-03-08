x,y,z=eval(input('请输入3个整数：中间用‘，’隔开：'))
if x>=y and x>=z:
    if z>y:
        print('%d%d%d'%(y,z,x))
    elif y>z:
        print('%d%d%d'%(z,y,x))
    else:
        print('%d%d%d'%(z,y,x))
elif y>=x and y>=z:
    if x>z:
        print('%d%d%d'%(z.x,y))
    elif z>x:
        print('%d%d%d'%(x,z,y))
    else:
        print('%d%d%d'%(z,x,y))
else:
    if x>y:
        print('%d%d%d'%(y,x,z))
    elif x<y:
        print('%d%d%d'%(x,y,z))
    else:
        print('%d%d%d'%(y,x,z))






    


