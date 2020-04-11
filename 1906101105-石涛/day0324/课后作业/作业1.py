# coding=utf-8

'''
给定一个不为空的链表，要求找到该链表的中间节点（若有两个中间值取第二个），然后输出中间值往后的链表
例如：[1，2，3，4，5]
输出：[3，4，5]
'''

'''这是力扣上的写法'''
# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         def length(): # 计算长度
#             cur=head
#             count=0
#             while cur!=None:
#                 count+=1
#                 cur=cur.next
#             return count

#         m=length()
#         p=head
#         n=m//2
#         while n>0:
#             p=p.next
#             n-=1
#         return p


'''这是可以测试的写法'''
# 节点类
class Node():
    def __init__(self,val):
        self.elem=val
        self.next=None

def search_middle(head): # 查询中间结点
    cur=head
    count=0
    while cur!=None:
        count+=1
        cur=cur.next

    p=head
    n=count//2
    while n>0:
        p=p.next
        n-=1
    return p

def node_print(head): # 打印结点
    l=[]
    cur=head
    while cur!=None:
        l.append(cur.elem)
        cur=cur.next
    return l

h=Node(0)
a=Node(1)
b=Node(2)
c=Node(3)
h.next=a
a.next=b
b.next=c
# print(search_middle(h))
print(node_print(h))
print(node_print(search_middle(h)))