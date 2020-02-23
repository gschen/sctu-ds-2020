import random
L=[14,25,98,75,23,1,4,46,59]
n=int(input())
m=int(input())
a=random.randint(1,len(L))
b=random.randint(1,len(L))
L[a]=n
L[b]=m
print(L)