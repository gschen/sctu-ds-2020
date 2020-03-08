x,y,z = map(int,input().split())
n = 0
l = [x,y,z]
def jiang(l,n):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
    if n == len(l):
        return l
    else:
        return jiang(l,n+1)
print(jiang(l,n))
