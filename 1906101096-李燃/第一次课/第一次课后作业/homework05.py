#交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
#要求，被置换的两个位置需要input输入


l = [14,25,98,75,23,1,4,56,59]
m,n = map(int,input().split())
if n<0 or m<0:
    print('错误')
if m<9 and n<9:
    l[m],l[n] = l[n],l[m]
print(l)