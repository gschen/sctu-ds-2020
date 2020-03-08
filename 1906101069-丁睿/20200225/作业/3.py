def qishu(*x):
    list=[]
    y=len(x)
    for i in range(0,y,2):
        list.append(x[i])
    print(list)
qishu(1,2,3,4,5,6,7)