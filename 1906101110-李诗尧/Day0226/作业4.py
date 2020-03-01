list=[1,2,3,4]
s=0
for i in list:
    for j in list:
        for n in list:
            if i!=j and j!=n and n!=i:
                s=s+1
                print(i+j*10+n*10*10)
print(s)
            
