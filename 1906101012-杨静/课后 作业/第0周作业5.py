#交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
#要求，被置换的两个位置需要input输入。

list0=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input().split())
list0[a],list0[b]=list0[b],list0[a]
print(list0)   