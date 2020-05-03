#作业1
#两数相加
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ''
        s2 = ''
        while l1:
            s1 = str(l1.val)+s1
            l1 = l1.next
        while l2:
            s2 = str(l2.val)+s2
            l2 = l2.next
        s3 = str(int(s1)+int(s2))
        l = len(s3)
        li = ListNode(int(s3[0]))
        for i in range(1,l):
            f = ListNode(int(s3[i]))
            f.next = li
            li = f 
        return li


#作业2
#合并K个排序链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = []
        for i in lists:
            while i:
                res.append(i.val)
                i = i.next
        res.sort()
        res_node = tem =ListNode(0)
        for j in res:
            tem.next = ListNode(j)
            tem = tem.next
        return res_node.next