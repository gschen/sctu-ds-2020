x,y,z=map(int,input().split())
l=[x,y,z]
def wu(l):
    for i in range(3):
        for j in range(2):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print(l)

wu(l)
