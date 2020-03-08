list1=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input().split())
list1[a-1],list1[b-1]=list1[b-1],list1[a-1]
print(list1)