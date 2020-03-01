def a3(arg):
    ret = [ ]
    for i in range(len(arg)):
        if i % 2 == 0:
            ret.append(arg[i])
        else:
            pass
    return ret
li = [1,2,3,4,5,6,7]
r = a3(li)
print(r)

