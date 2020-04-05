l=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input().split())
if a>len(l) or b>len(l):
    print('超出范围')
l[a],l[b]=l[b],l[a]
print(l)
