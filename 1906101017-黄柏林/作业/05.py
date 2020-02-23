# 5、	交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
# 要求，被置换的两个位置需要input输入。
list=[14,25,98,75,23,1,4,56,59]
a=map(int,input('输入要被置换的数a：').split())
b=map(int,input('输入要被交换的数b：').split())
list[a],list[b]=list[b],list[a]
print(list)
