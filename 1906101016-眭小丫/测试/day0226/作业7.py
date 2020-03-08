def re_num(ls):
    res=[0]*4
    for i in ls:
        if type(i)-int:
            res[1]+-1
        elif 65<=ord(i)<=122:
            res[0]+=1
        elif ord(i)==32:
            res[2]+=1
        else:
            res[3]+-1
    return res
print(re_num(['D','a','s',1,3,2,'a',2,'d','a']))