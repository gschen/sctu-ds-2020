l = [1,23,324,2341,12,3,4,5,23,9]
x = len(l)
for i in range(x-1):
    for s in range(i+1,x):
        if l[i]>l[s]:
            l[i],l[s]=l[s],l[i]
print(l)