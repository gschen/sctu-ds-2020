list=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input().split())
a_num=list[a+1]
b_num=list[b+1]
list[a+1]=b_num
list[b+1]=a_num
print(list)