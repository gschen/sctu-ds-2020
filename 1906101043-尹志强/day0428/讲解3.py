#Definition for a binary tree node
#class TreeNode:
#    def__init__(self,x):
#        self.val=x
#        self.next=None

class Solution:
    def mergeKLists(self,lists[ListNode]) -> ListNode:
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
        a=b=ListNode(1[0])
        for j in l[1:]:
            b.next=ListNode(j)
            b=b.next
        return a