a=0
for i in [1,2,3,4]:
    for y in [1,2,3,4]:
        for x in[1,2,3,4]:
            if i!=y and i!=x:
                a=a+1
                print('%d%d%d'%(i,y,x))
print('一共有%d个'%(a))
