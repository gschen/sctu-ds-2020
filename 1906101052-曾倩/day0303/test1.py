def res(ls):
    res=[0]*4
    for i in ls:
        if type(i)==int:
            res[1]=res[1]+1
        elif 65<=ord(i)<=90 and 97<=ord(i)<=122:
            res[0]=res[0]+1
        elif ord(i)==32:
            res[2]=res[2]+1
        else:
            res[3]+1
    return res
print(res(["D",'a',' ','s',1,2,3' ','a',1,'a']))
print(chr(97))