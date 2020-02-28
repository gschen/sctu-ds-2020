x,y=map(int,input().split())
l=[14,25,98,75,23,1,4,56,59]
a_x,a_y = l[x],l[y]
l[y],l[x] = a_x,a_y
print(l)