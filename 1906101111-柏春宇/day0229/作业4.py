a_set = [1,2,3,4]
for i in a_set:
    for j in a_set:
        for k in a_set:
            if i != j and i!=k and j!=k:
                print(i,j,k,end='')
                print()
