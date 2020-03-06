def list3(x):
        list1=[]
        for i in x:
            if int(i)%2!=0:
                list1.append(i)
        return list1

print(list3([1,2,3,4,5,6,7]))
            