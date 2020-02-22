list1=[14,25,98,75,23,1,4,56,59]
s=int(input("请输入一个位置："))
t=int(input("请输入一个位置："))
list1[s],list1[t]=list1[t],list1[s]
print(list1)