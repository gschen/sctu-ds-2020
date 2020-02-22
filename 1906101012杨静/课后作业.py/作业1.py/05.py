list=[14,25,98,75,23,1,4,56,59]
x,y=map(int,input().split())
list[x],list[y]=list[y],list[x]
print(list)