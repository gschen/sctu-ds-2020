def re(ls):
    re=[0]*4
    for i in ls:
        if 65<=ord(i)<=90 and 97<=ord(i)<=122:
            re[0]=re[0]+1
        elif 48<=ord(i)<=57:
            re[1]=re[1]+1
        elif ord(i)==32:
            re[2]=re[2]+1
        else:
            re[3]+=1
    return re
print(re(['D','a','','s',1,3,2]))
