a,b=map(int,input("请输入两个数").split( ))
lis=[14,25,98,75,23,1,4,56,59]
lis[a],lis[b] =  lis[b],lis[a]
print(lis)