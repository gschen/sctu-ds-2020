L=[14,25,98,75,23,1,4,56,59]
a=L.index(input())
b=L.index(input())
L[a],L[b]=L[b],L[a]
print(L)