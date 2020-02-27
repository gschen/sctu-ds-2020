a1, a2 = eval(input("请输入被置换的两个元素的位置(用逗号隔开)："))
def swap_position(lis,pos1,pos2):
    lis[pos1], lis[pos2] = lis[pos2], lis[pos1]
    return lis
lis = [14,25,98,75,23,1,4,56,59]
pos1, pos2 = a1, a2
print(swap_position(lis,pos1-1,pos2-1))
