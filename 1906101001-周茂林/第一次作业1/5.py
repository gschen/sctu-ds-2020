'''
交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
要求，被置换的两个位置需要input输入。
'''


a, b = map(int, input().split())
list1 = [14, 25, 98, 75, 23, 1, 4, 56, 59]
list1[b], list1[a] = list1[a], list1[b]
print(list1)
