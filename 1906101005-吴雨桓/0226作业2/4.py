l=[1,2,3,4]
l2=[]
def wu():
    for i in l:
        for j in l:
            for k in l:
                if i!=j and k!=j and i!=k:
                    l2.append(str(i)+str(j)+str(k))
    print("共有{}种组合，分别为{}".format(len(l2),l2))

wu()