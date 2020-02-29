#交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
#要求，被置换的两个位置需要input输入。


list0=[14,25,98,75,23,1,4,56,59]
m,n=map(int,input().split())
list0[m],list0[n]=list0[n],list0[m]
print(list0)    