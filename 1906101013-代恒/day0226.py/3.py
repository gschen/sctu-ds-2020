def look(x):
    list=[]
    for i in range(len(x)):
        if i % 2==0:
            list.append(x[i])
    return list



x=look([1,2,3,4,5,6,7])
print(x)