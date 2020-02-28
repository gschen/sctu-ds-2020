def list3(x):
    if type(x)==list:
        for i in x:
            if int(i)%2==0:
                x.remove(i)
            else:
                a=x
        return a
    if type(x)==tuple:
        list1=[]
        for i in x:
            if int(i)%2!=0:
                list1.append(i)
        return list1

print(list3((1,2,3,4,5,6,7)))
            