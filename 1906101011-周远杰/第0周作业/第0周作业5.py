#交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
#要求，被置换的两个位置需要input输入。


list1=[14,25,95,75,23,1,4,56,59]
m,n=map(int,input().split())
list1[m],list1[n]=list1[n],list1[m]
print(list1)