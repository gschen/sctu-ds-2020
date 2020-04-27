def jsw(l):
    l1 = []
    for i in range(len(l)):
        if i % 2 == 0: 
            l1.append(l[i])
    return l1
lis = [1,2,3,4,5,6,7]
print(jsw(lis))

    