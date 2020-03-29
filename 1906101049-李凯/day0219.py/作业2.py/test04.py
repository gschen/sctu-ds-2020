list=["1","2","3","4"]
for x in list:
    for y in list:
        for z in list:
            if x!=y and x!=z and y!=z:
                print(x+y+z)