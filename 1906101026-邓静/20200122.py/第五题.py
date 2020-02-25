#交换列表中得任意两个数
list=[14,25,98,75,23,1,4,56,59]
m,n=map(int,input().split())
list1_m,list1_n=list[m],list[n]
list[m],list[n]=list1_n,list1_m
print(list)