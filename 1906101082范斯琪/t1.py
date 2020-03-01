a=int(input('输入一个整数：'))
b=[1,10,20,30,40,50]
c=1
if a in b:
    print('False')
else:
    for i in range(1,a+1):
        c=c*i    
    print('此整数阶乘：%d'%(c))