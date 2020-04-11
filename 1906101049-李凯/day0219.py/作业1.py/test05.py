5、	交换列表中的任意两个元素：[14,25,98,75,23,1,4,56,59]
要求，被置换的两个位置需要input输入。

"""
list1 = [14,25,98,75,23,1,4,56,59]
m,n = map(int,input().split())
m_num = list1[m-1]
n_num = list1[n-1]

list1[m-1] = n_num
list1[n-1] = m_num
print(list1)
