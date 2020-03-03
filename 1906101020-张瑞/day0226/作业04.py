x1=[1,2,3,4]
x2=[1,2,3,4]
x3=[1,2,3,4]
l=[]
for x in x1:
    for y in x2:
        for z in x3:
            if x!=y!=z and y!=z!=x:
                a=x*100
                b=y*10
                c=a+b+z
                print(c)
              

   