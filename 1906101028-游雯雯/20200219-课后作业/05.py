list=[14,25,98,75,23,1,4,56,59]
a,b = map(int,input().split())
list[a],list[b] = list[b],list[a]
print(list)