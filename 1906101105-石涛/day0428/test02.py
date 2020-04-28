# coding=utf-8

'''
23. 合并K个排序链表

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists==[]:
            return lists
        l=[]
        for i in lists:
            while i:
                l.append(i.val)
                i=i.next
        l.sort()
        if l==[]:
            return lists
        a=b=ListNode(l[0])
        for j in l[1:]:
            b.next=ListNode(j)
            b=b.next
        return a