l1=[1,2,3,4]
l2=[]
for a in l1:
    for b in l1:
        for c in l1:
            if a!=b and b!=c and a!=c:
                d=a*100+b*10+c
                l2.append(d)
                s=len(l2)
print(l2)
print("可以组成%d个无重复三位数"%s)