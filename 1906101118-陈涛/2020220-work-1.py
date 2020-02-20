def jiecheng(a):
    if a==0:
        return 1
    elif a==10 or a==20:
        return "wrong"
    elif a==30 or a==40:
        return "wrong"
    elif a==50 or a==1:
        return "wrong"
    else:
        return (a*jiecheng(a-1))
asm=jiecheng(1) 
print(asm)       

            
