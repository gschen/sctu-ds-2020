'''5、交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
要求：被置换的两个位置需要input输入'''


list=[14,25,98,75,23,1,4,56,59]
x,y=map(int,input().split())
list[x],list[y]=list[y],list[x]
print(list)