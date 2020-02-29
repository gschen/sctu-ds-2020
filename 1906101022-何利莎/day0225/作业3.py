def js(*x):
    l=[]
    for i in x:
        if i % 2 == 1:
            l.append(i)
    print(l)
x=eval(input("输入几个数:"))#输入的数用逗号隔开
js(*x)