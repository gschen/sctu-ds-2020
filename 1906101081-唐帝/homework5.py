#交换列表中的任意两个元素






list=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input('请输入需要交换数字的位置,用逗号隔开：').split(','))
n=list[a]
m=list[b]
list[a]=m
list[b]=n
print(list)