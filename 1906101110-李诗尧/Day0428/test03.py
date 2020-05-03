# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ls=[]
        for i in lists:
            while i:
                ls.append(i.val)
                i=i.next
        ls.sort()
        ls_node=tem=ListNode(0)
        for j in ls:
            tem.next=ListNode(j)
            tem=tem.next
        return ls_node.next