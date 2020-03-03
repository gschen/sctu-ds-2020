x,y,z = map(str,input().split())
l = [x,y,z]
for i in range(0,3):
    for j in range(i,3):
        if int(l[i]) > int(l[j]):
            s = l[i]
            l[i] = l[j]
            l[j] = s

print(l)