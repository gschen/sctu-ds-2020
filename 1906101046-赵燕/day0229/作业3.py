def list(x):
    list1=[]
    for i in x:
        if i%2!=0:
            list1.append(i)
    return list1
print(list((1,2,3,4,5,6,7)))