def k(a):
    dic={'sz':0,'zm':0,'kg':0,'qt':0}
    for x in a:
        if x.isdigit():
            dic['sz']+=1
        elif x.isalpha():
            dic['zm']+=1
        elif x==' ':
            dic['kg']+=1
        else:
            dic['qt']+=1
        return dic
dic=k('D,a, ,s,1,3,2, ,a,2,d,a')
print(dic)